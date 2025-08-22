# Selenium Python - Page Objects Pattern Implementation

A comprehensive implementation of the **Page Objects** design pattern for Selenium WebDriver tests in Python, featuring an organized structure with separated locators for maximum maintainability and scalability.

## 🎯 **What is the Page Objects Pattern?**

The Page Objects pattern is a design pattern that:
- **Encapsulates** web page elements and their interactions
- **Separates** test logic from page interaction logic
- **Makes tests more maintainable** by centralizing element locators
- **Improves test readability** by using descriptive method names
- **Reduces code duplication** by reusing page object methods

## 🏗️ **Project Structure**

```
selenium-python/
├── api-automation/                    # 🆕 API Testing Package
│   └── tests/                        # API test files
│       ├── test_calculator.py        # Calculator function tests
│       └── test_reqres_api.py        # ReqRes API integration tests
├── locators/                          # 🆕 Dedicated locators package
│   ├── __init__.py                   # Package initialization
│   ├── landing_page_locators.py      # Landing page element locators
│   ├── search_results_locators.py    # Search results page locators
│   └── common_locators.py            # Common elements across pages
├── pages/                            # Page Objects package
│   ├── __init__.py                   # Package initialization
│   ├── base_page.py                  # Base page class with common functionality
│   ├── landing_page.py               # Landing page object (methods only)
│   └── search_results_page.py        # Search results page object (methods only)
├── src/                              # 🆕 Source code package
│   ├── calculator.py                 # Calculator functions for testing
│   └── api_utils.py                  # API testing utilities and client
├── test_with_page_objects.py         # Basic Page Objects test
├── test_page_objects_workflow.py     # Comprehensive workflow test
├── test_new_structure.py             # 🆕 New structure validation test
├── first_test.py                     # Original test (without Page Objects)
├── requirements.txt                   # 🆕 Python dependencies
└── README.md                         # This comprehensive guide
```

## 🔑 **Key Components**

### **1. Base Page Class (`pages/base_page.py`)**

The `BasePage` class provides common functionality that all page objects inherit:

- **Element finding methods**: `find_element()`, `find_elements()`
- **Wait methods**: `wait_for_element()`, `wait_for_element_clickable()`
- **Page information**: `get_title()`, `get_current_url()`
- **Navigation methods**: `navigate_to()`, `refresh_page()`

```python
from pages.base_page import BasePage

class MyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
```

### **2. Landing Page Object (`pages/landing_page.py`)**

The `LandingPage` class represents the BStack demo landing page:

- **Page Elements**: Search box, search icon, page title
- **Actions**: Load page, search for terms, verify page loaded
- **Verification**: Check element visibility, get page status

```python
from pages.landing_page import LandingPage

landing_page = LandingPage(driver)
landing_page.load()
landing_page.search_for("Selenium Python")
```

### **3. Search Results Page Object (`pages/search_results_page.py`)**

The `SearchResultsPage` class represents the search results page:

- **Page Elements**: Results container, result items, no results message
- **Actions**: Wait for results, click results, go back to search
- **Information**: Get results count, result titles, page status

```python
from pages.search_results_page import SearchResultsPage

search_results = SearchResultsPage(driver)
results_count = search_results.get_results_count()
```

## 📍 **Locators Organization**

### **Separated Locator Files**

We've organized locators into dedicated files for better maintainability:

#### **`locators/landing_page_locators.py`**
```python
from selenium.webdriver.common.by import By

class LandingPageLocators:
    # Search functionality
    SEARCH_BOX = (By.XPATH, "//*[@placeholder='Search']")
    SEARCH_ICON = (By.XPATH, "//*[text()='Search']")
    
    # Page structure elements
    PAGE_TITLE = (By.TAG_NAME, "title")
    HEADER = (By.TAG_NAME, "header")
    
    # Additional UI elements
    NAVIGATION_MENU = (By.CLASS_NAME, "nav-menu")
    USER_MENU = (By.CLASS_NAME, "user-menu")
```

#### **`locators/search_results_locators.py`**
```python
class SearchResultsPageLocators:
    # Search results container
    SEARCH_RESULTS_CONTAINER = (By.CLASS_NAME, "search-results")
    SEARCH_RESULTS_LIST = (By.CLASS_NAME, "result-item")
    
    # Result item elements
    RESULT_TITLE = (By.CLASS_NAME, "result-title")
    RESULT_DESCRIPTION = (By.CLASS_NAME, "result-description")
    
    # Pagination and filters
    NEXT_PAGE_BUTTON = (By.CLASS_NAME, "next-page")
    FILTER_SIDEBAR = (By.CLASS_NAME, "filter-sidebar")
```

#### **`locators/common_locators.py`**
```python
class CommonLocators:
    # Common navigation elements
    HOME_LINK = (By.CLASS_NAME, "home-link")
    LOGO = (By.CLASS_NAME, "logo")
    
    # Common UI elements
    LOADING_SPINNER = (By.CLASS_NAME, "loading-spinner")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    
    # Common buttons
    SUBMIT_BUTTON = (By.CLASS_NAME, "submit-button")
    LOGIN_BUTTON = (By.CLASS_NAME, "login-button")
```

## 🚀 **How to Use**

### **Basic Usage**

```python
from selenium import webdriver
from pages.landing_page import LandingPage

# Setup driver
driver = webdriver.Chrome()

# Create page object
landing_page = LandingPage(driver)

# Use page object methods
landing_page.load()
landing_page.search_for("Selenium Python")
title = landing_page.get_page_title()

# Cleanup
driver.quit()
```

### **Complete Workflow Example**

```python
# Load landing page
landing_page = LandingPage(driver)
landing_page.load()

# Perform search
landing_page.search_for("Python")

# Handle search results
search_results = SearchResultsPage(driver)
results_count = search_results.get_results_count()
```

### **Using Locators Directly**

```python
from locators.landing_page_locators import LandingPageLocators
from locators.common_locators import CommonLocators

# Access specific locators
search_box_locator = LandingPageLocators.SEARCH_BOX
home_link_locator = CommonLocators.HOME_LINK
```

## ✅ **Benefits of This Implementation**

### **1. Maintainability**
- Element locators are centralized in dedicated files
- Changes to page elements only require updates in one place
- Tests remain unchanged when page structure changes

### **2. Readability**
- Test methods read like natural language
- Clear separation of concerns
- Descriptive method names

### **3. Reusability**
- Page objects can be used across multiple tests
- Common functionality is inherited from base class
- Easy to extend with new page objects

### **4. Reliability**
- Built-in wait mechanisms for elements
- Proper error handling and verification
- Consistent interaction patterns

### **5. Organization**
- **Separated concerns**: Locators vs. page logic
- **Dedicated files**: Each page has its own locator file
- **Common elements**: Shared locators in a separate file
- **Clear structure**: Easy to navigate and understand

## 🧪 **Running the Tests**

### **Prerequisites**

1. **Install Python 3.6+**
2. **Install Selenium**: `pip install selenium`
3. **Install Chrome WebDriver** (or use Selenium Manager)

### **Setup Virtual Environment**

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows

# Install dependencies
pip install selenium
```

### **Running Tests**

```bash
# Activate virtual environment
source venv/bin/activate

# Basic Page Objects test
python test_with_page_objects.py

# Comprehensive workflow test
python test_page_objects_workflow.py

# New structure validation test
python test_new_structure.py

# Original test (for comparison)
python first_test.py
```

## 🔧 **Best Practices Demonstrated**

### **1. Locator Management**
```python
# Good: Centralized locators as class variables
SEARCH_BOX = (By.XPATH, "//*[@placeholder='Search']")
SEARCH_ICON = (By.XPATH, "//*[text()='Search']")

# Usage
search_box = self.find_element(LandingPageLocators.SEARCH_BOX)
```

### **2. Wait Strategies**
```python
# Wait for element to be present and clickable
search_box = self.wait_for_element_clickable(LandingPageLocators.SEARCH_BOX)
```

### **3. Page Verification**
```python
def verify_page_loaded(self):
    """Verify that the landing page has loaded correctly."""
    assert "StackDemo" in self.get_title()
    return True
```

### **4. Error Handling**
```python
def is_search_box_visible(self):
    """Check if the search box is visible on the page."""
    try:
        self.wait_for_element(LandingPageLocators.SEARCH_BOX, timeout=5)
        return True
    except:
        return False
```

## 🚀 **Extending the Pattern**

### **Adding New Page Objects**

1. **Create a new locator file** in the `locators/` directory
2. **Create a new page class** that inherits from `BasePage`
3. **Define page elements** as class variables using locators
4. **Implement page actions** as methods
5. **Add verification methods** for page state

### **Example: Adding a Product Details Page**

```python
# locators/product_page_locators.py
class ProductPageLocators:
    PRODUCT_TITLE = (By.CLASS_NAME, "product-title")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "add-to-cart")
    PRODUCT_IMAGE = (By.CLASS_NAME, "product-image")

# pages/product_page.py
from locators.product_page_locators import ProductPageLocators

class ProductPage(BasePage):
    def get_product_title(self):
        """Get the product title."""
        return self.find_element(ProductPageLocators.PRODUCT_TITLE).text
    
    def add_to_cart(self):
        """Add the product to cart."""
        self.find_element(ProductPageLocators.ADD_TO_CART_BUTTON).click()
```

### **Adding New Locators**

```python
# locators/landing_page_locators.py
class LandingPageLocators:
    # Existing locators...
    
    # New locators
    NEWSLETTER_SIGNUP = (By.ID, "newsletter-signup")
    SOCIAL_MEDIA_LINKS = (By.CLASS_NAME, "social-media-link")
    COOKIE_BANNER = (By.CLASS_NAME, "cookie-banner")
```

## 🆕 **API Automation Testing**

This project now includes comprehensive API testing capabilities alongside the existing Selenium WebDriver tests.

### **API Testing Features**

- **REST API Testing**: Full CRUD operations testing
- **JSON Schema Validation**: Automatic response structure validation
- **Performance Testing**: Response time and concurrent request testing
- **Data Integrity**: Comprehensive data validation and consistency checks
- **Error Handling**: Proper error response validation
- **Authentication**: API key-based authentication support

### **API Testing Structure**

#### **`src/api_utils.py`**
The core API testing utilities providing:

- **APIClient**: HTTP client with authentication and session management
- **APIResponse**: Response wrapper with assertion methods
- **Schema Validation**: JSON schema validation utilities
- **User Schema Validation**: Specific validation for user data structures

```python
from src.api_utils import APIClient, validate_user_schema

# Create API client
api_client = APIClient("https://reqres.in")

# Make requests
response = api_client.get("/api/users", params={"page": 2})

# Assertions
response.assert_status_code(200)
response.assert_contains_key("data")
response.assert_response_time(5000)  # 5 seconds max
```

#### **`api-automation/tests/test_calculator.py`**
Unit tests for calculator functions:

- **Basic Operations**: Addition, subtraction, multiplication, division
- **Edge Cases**: Division by zero, negative numbers
- **Floating Point**: Precision testing with pytest.approx
- **Square Function**: Testing mathematical operations

```python
def test_add_floats():
    """Test addition with floating point numbers."""
    assert add(2.5, 3.5) == 6.0
    assert add(0.1, 0.2) == pytest.approx(0.3, rel=1e-9)
```

#### **`api-automation/tests/test_reqres_api.py`**
Comprehensive API integration tests:

- **User Management**: CRUD operations for users
- **Pagination**: Page-based user listing
- **Data Validation**: Schema and data integrity checks
- **Performance**: Response time and concurrent request testing
- **Error Handling**: Invalid requests and edge cases

### **API Testing Capabilities**

#### **1. HTTP Methods Support**
```python
# GET requests
response = api_client.get("/api/users", params={"page": 2})

# POST requests
response = api_client.post("/api/users", data={"name": "John", "job": "Engineer"})

# PUT requests
response = api_client.put("/api/users/1", data={"name": "Jane", "job": "Manager"})

# DELETE requests
response = api_client.delete("/api/users/1")
```

#### **2. Response Assertions**
```python
# Status code assertions
response.assert_status_code(200)

# Key presence assertions
response.assert_contains_key("data")

# Value assertions
response.assert_key_value("page", 2)

# Response time assertions
response.assert_response_time(3000)  # 3 seconds max

# JSON schema validation
response.assert_json_schema(expected_schema)
```

#### **3. Data Validation**
```python
# User schema validation
for user in response.json["data"]:
    assert validate_user_schema(user), f"Invalid user schema: {user}"

# Data integrity checks
user_ids = [user["id"] for user in data]
assert len(user_ids) == len(set(user_ids)), "User IDs should be unique"
```

#### **4. Performance Testing**
```python
# Concurrent request testing
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(make_request) for _ in range(5)]
    results = [future.result() for future in futures]

# Response time consistency
response_times = []
for _ in range(3):
    response = api_client.get("/api/users", params={"page": 1})
    response_time = response.response.elapsed.total_seconds()
    response_times.append(response_time)
```

### **Running API Tests**

#### **Prerequisites**
```bash
# Install dependencies
pip install -r requirements.txt

# Required packages:
# - pytest>=7.0.0
# - pytest-cov>=4.0.0
# - pytest-html>=3.0.0
# - pytest-xdist>=3.0.0
# - requests>=2.31.0
# - jsonschema>=4.19.0
```

#### **Running Tests**
```bash
# Run calculator tests
python -m pytest api-automation/tests/test_calculator.py -v

# Run API integration tests
python -m pytest api-automation/tests/test_reqres_api.py -v

# Run all API tests
python -m pytest api-automation/tests/ -v

# Run with coverage
python -m pytest api-automation/tests/ --cov=src

# Run with HTML report
python -m pytest api-automation/tests/ --html=api_report.html
```

### **API Testing Best Practices**

#### **1. Test Organization**
```python
class TestReqResAPI:
    """Test class for ReqRes API endpoints."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup API client for each test."""
        self.api_client = APIClient("https://reqres.in")
```

#### **2. Comprehensive Assertions**
```python
def test_get_users_page_2(self):
    """Test GET /api/users?page=2 endpoint."""
    response = self.api_client.get("/api/users", params={"page": 2})
    
    # Multiple assertion types
    response.assert_status_code(200)
    response.assert_response_time(5000)
    response.assert_contains_key("data")
    response.assert_key_value("page", 2)
```

#### **3. Data Validation**
```python
# Validate response structure
response.assert_json_schema(users_schema)

# Validate individual items
for user in response.json["data"]:
    assert validate_user_schema(user)
```

#### **4. Performance Considerations**
```python
# Set reasonable timeouts
response.assert_response_time(3000)  # 3 seconds max

# Test concurrent requests
# Test response time consistency
# Test under load conditions
```

### **Extending API Testing**

#### **Adding New API Endpoints**
```python
def test_new_endpoint(self):
    """Test a new API endpoint."""
    response = self.api_client.get("/api/new-endpoint")
    
    response.assert_status_code(200)
    response.assert_contains_key("expected_key")
    
    # Add specific business logic validation
    data = response.json["data"]
    assert len(data) > 0, "Should return data"
```

#### **Adding New Validation Schemas**
```python
def validate_product_schema(response_data: Dict[str, Any]):
    """Validate product data structure."""
    product_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "price": {"type": "number"},
            "category": {"type": "string"}
        },
        "required": ["id", "name", "price", "category"]
    }
    
    try:
        validate(instance=response_data, schema=product_schema)
        return True
    except ValidationError:
        return False
```

## 🔍 **Common Locator Strategies**

### **1. ID (Most reliable)**
```python
USERNAME_FIELD = (By.ID, "username")
```

### **2. CSS Selector (Good balance)**
```python
SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
```

### **3. XPath (Most flexible)**
```python
SEARCH_BOX = (By.XPATH, "//*[@placeholder='Search']")
```

### **4. Class Name (Quick but fragile)**
```python
RESULT_ITEM = (By.CLASS_NAME, "result-item")
```

### **5. Link Text (For links)**
```python
HOME_LINK = (By.LINK_TEXT, "Home")
```

## 🚀 **Running All Tests**

### **Complete Test Suite**
```bash
# Activate virtual environment
source venv/bin/activate

# Run Selenium tests
python test_with_page_objects.py
python test_page_objects_workflow.py
python test_new_structure.py

# Run API tests
python -m pytest api-automation/tests/ -v

# Run with coverage
python -m pytest api-automation/tests/ --cov=src --cov-report=html
```

### **Test Reports**
- **Console Output**: Detailed test results with pytest
- **HTML Reports**: `pytest --html=report.html`
- **Coverage Reports**: `pytest --cov=src --cov-report=html`
- **Parallel Execution**: `pytest -n auto` for faster execution

**Happy testing! 🚀**
