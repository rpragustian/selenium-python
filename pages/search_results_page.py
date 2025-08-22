#!/usr/bin/env python3
"""
Search Results Page Object class for BStack Demo application.
This class represents the page that appears after performing a search.
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import SearchResultsPageLocators


class SearchResultsPage(BasePage):
    """Search results page object for BStack Demo application."""
    
    def __init__(self, driver):
        """Initialize the search results page with a webdriver instance."""
        super().__init__(driver)
    
    def wait_for_results_to_load(self):
        """Wait for search results to load on the page."""
        try:
            self.wait_for_element(SearchResultsPageLocators.SEARCH_RESULTS_CONTAINER, timeout=10)
            return True
        except:
            return False
    
    def get_results_count(self):
        """Get the number of search results displayed."""
        try:
            results = self.find_elements(SearchResultsPageLocators.SEARCH_RESULTS_LIST)
            return len(results)
        except:
            return 0
    
    def get_result_titles(self):
        """Get the titles of all search results."""
        try:
            results = self.find_elements(SearchResultsPageLocators.SEARCH_RESULTS_LIST)
            titles = []
            for result in results:
                title_element = result.find_element(By.CLASS_NAME, "result-title")
                titles.append(title_element.text)
            return titles
        except:
            return []
    
    def click_first_result(self):
        """Click on the first search result."""
        try:
            first_result = self.find_element(SearchResultsPageLocators.SEARCH_RESULTS_LIST)
            first_result.click()
            return True
        except:
            return False
    
    def is_no_results_displayed(self):
        """Check if the 'no results' message is displayed."""
        try:
            self.wait_for_element(SearchResultsPageLocators.NO_RESULTS_MESSAGE, timeout=5)
            return True
        except:
            return False
    
    def go_back_to_search(self):
        """Click the back to search button."""
        try:
            back_button = self.find_element(SearchResultsPageLocators.BACK_TO_SEARCH_BUTTON)
            back_button.click()
            return True
        except:
            return False
    
    def get_page_info(self):
        """Get comprehensive information about the search results page."""
        return {
            "results_loaded": self.wait_for_results_to_load(),
            "results_count": self.get_results_count(),
            "result_titles": self.get_result_titles(),
            "no_results_displayed": self.is_no_results_displayed(),
            "page_title": self.get_page_title(),
            "current_url": self.get_current_url()
        }
