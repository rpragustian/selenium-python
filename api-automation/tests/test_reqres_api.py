"""
API tests for ReqRes API (https://reqres.in)
"""

import pytest
from src.api_utils import APIClient, validate_user_schema


class TestReqResAPI:
    """Test class for ReqRes API endpoints."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup API client for each test."""
        self.api_client = APIClient("https://reqres.in")
    
    def test_get_users_page_2(self):
        """Test GET /api/users?page=2 endpoint - equivalent to your curl command."""
        # Make the API request
        response = self.api_client.get("/api/users", params={"page": 2})
        
        # Assert basic response properties
        response.assert_status_code(200)
        response.assert_response_time(5000)  # 5 seconds max
        
        # Assert response structure
        response.assert_contains_key("page")
        response.assert_contains_key("per_page")
        response.assert_contains_key("total")
        response.assert_contains_key("total_pages")
        response.assert_contains_key("data")
        response.assert_contains_key("support")
        
        # Assert specific values
        response.assert_key_value("page", 2)
        response.assert_key_value("per_page", 6)
        response.assert_key_value("total_pages", 2)
        
        # Validate data array
        data = response.json["data"]
        assert isinstance(data, list), "Data should be a list"
        assert len(data) == 6, f"Expected 6 users, got {len(data)}"
        
        # Validate each user object
        for user in data:
            assert validate_user_schema(user), f"Invalid user schema: {user}"
    
    def test_get_users_page_1(self):
        """Test GET /api/users?page=1 endpoint."""
        response = self.api_client.get("/api/users", params={"page": 1})
        
        response.assert_status_code(200)
        response.assert_key_value("page", 1)
        
        data = response.json["data"]
        assert len(data) == 6, f"Expected 6 users, got {len(data)}"
    
    def test_get_users_invalid_page(self):
        """Test GET /api/users with invalid page number."""
        # Note: ReqRes API now returns 401 for very high page numbers
        # Let's test with a reasonable but non-existent page
        response = self.api_client.get("/api/users", params={"page": 10})
        
        # Should return 200 with empty data for reasonable page numbers
        response.assert_status_code(200)
        response.assert_key_value("page", 10)
        
        # Should return empty data for non-existent page
        data = response.json["data"]
        assert len(data) == 0, "Non-existent page should return empty data"
    
    def test_get_users_no_page_param(self):
        """Test GET /api/users without page parameter (defaults to page 1)."""
        response = self.api_client.get("/api/users")
        
        response.assert_status_code(200)
        response.assert_key_value("page", 1)
        
        data = response.json["data"]
        assert len(data) == 6, "Default page should return 6 users"
    
    def test_get_users_with_per_page_param(self):
        """Test GET /api/users with per_page parameter."""
        # With API key authentication, per_page parameter now works
        response = self.api_client.get("/api/users", params={"page": 1, "per_page": 3})
        
        response.assert_status_code(200)
        response.assert_key_value("per_page", 3)
        
        data = response.json["data"]
        assert len(data) == 3, f"Expected 3 users, got {len(data)}"
    
    def test_get_users_response_headers(self):
        """Test that response headers are properly set."""
        response = self.api_client.get("/api/users", params={"page": 2})
        
        response.assert_status_code(200)
        
        # Check important headers
        headers = response.headers
        assert "content-type" in headers, "Response should have content-type header"
        assert "application/json" in headers["content-type"], "Content type should be JSON"
    
    def test_get_users_data_integrity(self):
        """Test data integrity and consistency."""
        response = self.api_client.get("/api/users", params={"page": 2})
        
        response.assert_status_code(200)
        
        data = response.json["data"]
        total = response.json["total"]
        per_page = response.json["per_page"]
        total_pages = response.json["total_pages"]
        
        # Validate mathematical relationships
        assert total_pages == (total + per_page - 1) // per_page, "Total pages calculation is incorrect"
        
        # Validate user IDs are unique and sequential
        user_ids = [user["id"] for user in data]
        assert len(user_ids) == len(set(user_ids)), "User IDs should be unique"
        
        # Validate email format for each user
        for user in data:
            email = user["email"]
            assert "@" in email, f"Invalid email format: {email}"
            assert "." in email.split("@")[1], f"Invalid email domain: {email}"
    
    def test_get_users_performance(self):
        """Test API response time performance."""
        response = self.api_client.get("/api/users", params={"page": 2})
        
        response.assert_status_code(200)
        response.assert_response_time(3000)  # 3 seconds max for good performance
    
    def test_get_users_json_schema(self):
        """Test that response matches expected JSON schema."""
        response = self.api_client.get("/api/users", params={"page": 2})
        
        response.assert_status_code(200)
        
        # Define expected schema for the users list response
        users_schema = {
            "type": "object",
            "properties": {
                "page": {"type": "integer"},
                "per_page": {"type": "integer"},
                "total": {"type": "integer"},
                "total_pages": {"type": "integer"},
                "data": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "email": {"type": "string"},
                            "first_name": {"type": "string"},
                            "last_name": {"type": "string"},
                            "avatar": {"type": "string"}
                        },
                        "required": ["id", "email", "first_name", "last_name", "avatar"]
                    }
                },
                "support": {
                    "type": "object",
                    "properties": {
                        "url": {"type": "string"},
                        "text": {"type": "string"}
                    },
                    "required": ["url", "text"]
                }
            },
            "required": ["page", "per_page", "total", "total_pages", "data", "support"]
        }
        
        response.assert_json_schema(users_schema)


# Test individual user endpoints
class TestIndividualUserEndpoints:
    """Test individual user CRUD operations."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup API client for each test."""
        self.api_client = APIClient("https://reqres.in")
    
    def test_get_single_user(self):
        """Test GET /api/users/{id} endpoint."""
        response = self.api_client.get("/api/users/1")
        
        response.assert_status_code(200)
        response.assert_contains_key("data")
        
        user = response.json["data"]
        assert validate_user_schema(user), f"Invalid user schema: {user}"
        assert user["id"] == 1, f"Expected user ID 1, got {user['id']}"
    
    def test_get_nonexistent_user(self):
        """Test GET /api/users/{id} with non-existent user ID."""
        # With API key, the API now returns 404 for non-existent users (correct behavior)
        response = self.api_client.get("/api/users/999")
        
        response.assert_status_code(404)
    
    def test_get_user_edge_cases(self):
        """Test GET /api/users/{id} with edge case IDs."""
        # Test with ID 0 (should return 404 as it doesn't exist)
        response = self.api_client.get("/api/users/0")
        response.assert_status_code(404)
        
        # Test with ID 12 (last user in the dataset)
        response = self.api_client.get("/api/users/12")
        response.assert_status_code(200)
        response.assert_contains_key("data")
        
        user = response.json["data"]
        assert user["id"] == 12, f"Expected user ID 12, got {user['id']}"
    
    def test_create_user(self):
        """Test POST /api/users endpoint."""
        user_data = {
            "name": "John Doe",
            "job": "Software Engineer"
        }
        
        response = self.api_client.post("/api/users", data=user_data)
        
        response.assert_status_code(201)
        response.assert_contains_key("name")
        response.assert_contains_key("job")
        response.assert_contains_key("id")
        response.assert_contains_key("createdAt")
        
        # Validate response data
        response.assert_key_value("name", "John Doe")
        response.assert_key_value("job", "Software Engineer")
    
    def test_update_user(self):
        """Test PUT /api/users/{id} endpoint."""
        user_data = {
            "name": "Jane Smith",
            "job": "Product Manager"
        }
        
        response = self.api_client.put("/api/users/1", data=user_data)
        
        response.assert_status_code(200)
        response.assert_key_value("name", "Jane Smith")
        response.assert_key_value("job", "Product Manager")
        response.assert_contains_key("updatedAt")
    
    def test_delete_user(self):
        """Test DELETE /api/users/{id} endpoint."""
        response = self.api_client.delete("/api/users/1")
        
        response.assert_status_code(204)
        assert response.text == "", "Delete response should be empty"


# Test API behavior and edge cases
class TestAPIBehavior:
    """Test various API behaviors and edge cases."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup API client for each test."""
        self.api_client = APIClient("https://reqres.in")
    
    def test_api_rate_limiting(self):
        """Test that API doesn't have aggressive rate limiting."""
        responses = []
        
        # Make 3 quick requests
        for i in range(3):
            response = self.api_client.get("/api/users", params={"page": 1})
            responses.append(response)
        
        # All should succeed
        for response in responses:
            response.assert_status_code(200)
    
    def test_api_error_handling(self):
        """Test API error handling for malformed requests."""
        # Test with invalid query parameters
        response = self.api_client.get("/api/users", params={"invalid_param": "value"})
        
        # Should still return 200, just ignore invalid params
        response.assert_status_code(200)
    
    def test_api_response_consistency(self):
        """Test that API responses are consistent."""
        # Make the same request twice
        response1 = self.api_client.get("/api/users", params={"page": 1})
        response2 = self.api_client.get("/api/users", params={"page": 1})
        
        response1.assert_status_code(200)
        response2.assert_status_code(200)
        
        # Both responses should have the same structure
        assert response1.json.keys() == response2.json.keys(), "Response structure should be consistent"
        
        # Page numbers should be the same
        assert response1.json["page"] == response2.json["page"], "Page numbers should be consistent"


# Performance and load testing
class TestAPIPerformance:
    """Test API performance under various conditions."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup API client for each test."""
        self.api_client = APIClient("https://reqres.in")
    
    def test_multiple_concurrent_requests(self):
        """Test multiple concurrent requests to the same endpoint."""
        import concurrent.futures
        import time
        
        def make_request():
            start_time = time.time()
            response = self.api_client.get("/api/users", params={"page": 1})
            end_time = time.time()
            return response, end_time - start_time
        
        # Make 5 concurrent requests
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(make_request) for _ in range(5)]
            results = [future.result() for future in futures]
        
        # Validate all responses
        for response, response_time in results:
            response.assert_status_code(200)
            assert response_time < 5.0, f"Response time {response_time:.2f}s exceeds 5s limit"
    
    def test_response_time_consistency(self):
        """Test that response times are consistent across multiple requests."""
        response_times = []
        
        for _ in range(3):
            response = self.api_client.get("/api/users", params={"page": 1})
            response.assert_status_code(200)
            response_time = response.response.elapsed.total_seconds()
            response_times.append(response_time)
        
        # Check that response times are reasonably consistent
        avg_time = sum(response_times) / len(response_times)
        max_deviation = max(abs(t - avg_time) for t in response_times)
        
        assert max_deviation < 2.0, f"Response time deviation {max_deviation:.2f}s is too high"
    
    def test_api_endpoint_performance_comparison(self):
        """Compare performance of different endpoints."""
        endpoints = [
            ("/api/users", {"page": 1}),
            ("/api/users", {"page": 2}),
            ("/api/users/1", {}),
            ("/api/users/2", {})
        ]
        
        performance_data = {}
        
        for endpoint, params in endpoints:
            response = self.api_client.get(endpoint, params=params)
            response.assert_status_code(200)
            
            response_time = response.response.elapsed.total_seconds()
            performance_data[endpoint] = response_time
            
            # Each endpoint should respond within reasonable time
            assert response_time < 3.0, f"Endpoint {endpoint} too slow: {response_time:.2f}s"
        
        print(f"Performance comparison: {performance_data}")