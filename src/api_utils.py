"""
API testing utilities for making HTTP requests and validating responses.
"""

import requests
import json
from typing import Dict, Any, Optional
from jsonschema import validate, ValidationError


class APIClient:
    """Base API client for making HTTP requests."""
    
    def __init__(self, base_url: str = "https://reqres.in"):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': 'Pytest-API-Testing/1.0',
            'x-api-key': 'reqres-free-v1'  # ReqRes API authentication
        })
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None, **kwargs):
        """Make a GET request."""
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params, **kwargs)
        return APIResponse(response)
    
    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None, **kwargs):
        """Make a POST request."""
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, json=data, **kwargs)
        return APIResponse(response)
    
    def put(self, endpoint: str, data: Optional[Dict[str, Any]] = None, **kwargs):
        """Make a PUT request."""
        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, json=data, **kwargs)
        return APIResponse(response)
    
    def delete(self, endpoint: str, **kwargs):
        """Make a DELETE request."""
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url, **kwargs)
        return APIResponse(response)


class APIResponse:
    """Wrapper for API responses with useful methods."""
    
    def __init__(self, response: requests.Response):
        self.response = response
        self.status_code = response.status_code
        self.headers = response.headers
        self._json = None
    
    @property
    def json(self):
        """Get JSON response data."""
        if self._json is None:
            try:
                self._json = self.response.json()
            except json.JSONDecodeError:
                self._json = {}
        return self._json
    
    @property
    def text(self):
        """Get response text."""
        return self.response.text
    
    def assert_status_code(self, expected_code: int):
        """Assert that the response has the expected status code."""
        assert self.status_code == expected_code, \
            f"Expected status code {expected_code}, got {self.status_code}"
    
    def assert_json_schema(self, schema: Dict[str, Any]):
        """Assert that the response matches the expected JSON schema."""
        try:
            validate(instance=self.json, schema=schema)
        except ValidationError as e:
            assert False, f"JSON schema validation failed: {e.message}"
    
    def assert_contains_key(self, key: str):
        """Assert that the response contains a specific key."""
        assert key in self.json, f"Response does not contain key '{key}'"
    
    def assert_key_value(self, key: str, expected_value: Any):
        """Assert that a specific key has the expected value."""
        self.assert_contains_key(key)
        assert self.json[key] == expected_value, \
            f"Expected {key}={expected_value}, got {key}={self.json[key]}"
    
    def assert_response_time(self, max_time_ms: int):
        """Assert that the response time is within acceptable limits."""
        response_time_ms = self.response.elapsed.total_seconds() * 1000
        assert response_time_ms <= max_time_ms, \
            f"Response time {response_time_ms:.2f}ms exceeds limit {max_time_ms}ms"


def validate_user_schema(response_data: Dict[str, Any]):
    """Validate user data structure from ReqRes API."""
    user_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "email": {"type": "string", "format": "email"},
            "first_name": {"type": "string"},
            "last_name": {"type": "string"},
            "avatar": {"type": "string", "format": "uri"}
        },
        "required": ["id", "email", "first_name", "last_name", "avatar"]
    }
    
    try:
        validate(instance=response_data, schema=user_schema)
        return True
    except ValidationError:
        return False