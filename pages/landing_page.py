#!/usr/bin/env python3
"""
Landing Page Object class for BStack Demo application.
This class represents the landing page and contains all the page elements
and actions that can be performed on this page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from .locators import LandingPageLocators


class LandingPage(BasePage):
    """Landing page object for BStack Demo application."""
    
    def __init__(self, driver):
        """Initialize the landing page with a webdriver instance."""
        super().__init__(driver)
        self.url = "https://www.bstackdemo.com/"
    
    def load(self):
        """Load the landing page."""
        self.navigate_to(self.url)
        self.wait_for_element(LandingPageLocators.SEARCH_BOX)
    
    def get_page_title(self):
        """Get the page title text."""
        return self.get_title()
    
    def verify_page_loaded(self):
        """Verify that the landing page has loaded correctly."""
        assert "StackDemo" in self.get_title(), f"Expected 'StackDemo' in title, got: {self.get_title()}"
        return True
    
    def search_for(self, search_term):
        """Search for a specific term using the search functionality."""
        self.find_element(LandingPageLocators.SEARCH_BOX).send_keys(search_term)
        self.find_element(LandingPageLocators.SEARCH_ICON).click()
    
    def get_search_box_text(self):
        """Get the text of the search box."""
        return self.find_element(LandingPageLocators.SEARCH_BOX).text
    
    def clear_search(self):
        """Clear the search box."""
        search_box = self.find_element(LandingPageLocators.SEARCH_BOX)
        search_box.clear()
    
    def is_search_box_visible(self):
        """Check if the search box is visible on the page."""
        try:
            self.wait_for_element(LandingPageLocators.SEARCH_BOX, timeout=5)
            return True
        except:
            return False
    
    def is_search_icon_visible(self):
        """Check if the search icon is visible on the page."""
        try:
            self.wait_for_element(LandingPageLocators.SEARCH_ICON, timeout=5)
            return True
        except:
            return False
    
    def get_page_elements_status(self):
        """Get the status of key page elements."""
        return {
            "search_box_visible": self.is_search_box_visible(),
            "search_icon_visible": self.is_search_icon_visible(),
            "page_title": self.get_page_title(),
            "current_url": self.get_current_url()
        }