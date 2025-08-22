#!/usr/bin/env python3
"""
Base Page Object class that provides common functionality
for all page objects in the application.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    """Base page object class with common methods."""
    
    def __init__(self, driver):
        """Initialize the base page with a webdriver instance."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        """Find a single element using the provided locator."""
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        """Find multiple elements using the provided locator."""
        return self.driver.find_elements(*locator)
    
    def wait_for_element(self, locator, timeout=10):
        """Wait for an element to be present and visible."""
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )
    
    def wait_for_element_clickable(self, locator, timeout=10):
        """Wait for an element to be clickable."""
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )
    
    def get_title(self):
        """Get the current page title."""
        return self.driver.title
    
    def get_current_url(self):
        """Get the current page URL."""
        return self.driver.current_url
    
    def navigate_to(self, url):
        """Navigate to a specific URL."""
        self.driver.get(url)
    
    def refresh_page(self):
        """Refresh the current page."""
        self.driver.refresh()
