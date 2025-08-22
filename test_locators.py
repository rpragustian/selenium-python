#!/usr/bin/env python3
"""
Simple test to demonstrate that the locators are working properly.
This test shows how the separate locators file is being used.
"""

from selenium import webdriver
from pages.locators import LandingPageLocators, SearchResultsPageLocators, CommonLocators


def test_locators_import():
    """Test that all locators can be imported and accessed."""
    print("=== Testing Locators Import ===\n")
    
    # Test Landing Page Locators
    print("Landing Page Locators:")
    print(f"  SEARCH_BOX: {LandingPageLocators.SEARCH_BOX}")
    print(f"  SEARCH_ICON: {LandingPageLocators.SEARCH_ICON}")
    print(f"  PAGE_TITLE: {LandingPageLocators.PAGE_TITLE}")
    print(f"  HEADER: {LandingPageLocators.HEADER}")
    print(f"  MAIN_CONTENT: {LandingPageLocators.MAIN_CONTENT}")
    print(f"  FOOTER: {LandingPageLocators.FOOTER}")
    
    print("\nSearch Results Page Locators:")
    print(f"  SEARCH_RESULTS_CONTAINER: {SearchResultsPageLocators.SEARCH_RESULTS_CONTAINER}")
    print(f"  SEARCH_RESULTS_LIST: {SearchResultsPageLocators.SEARCH_RESULTS_LIST}")
    print(f"  RESULT_TITLE: {SearchResultsPageLocators.RESULT_TITLE}")
    print(f"  NO_RESULTS_MESSAGE: {SearchResultsPageLocators.NO_RESULTS_MESSAGE}")
    print(f"  BACK_TO_SEARCH_BUTTON: {SearchResultsPageLocators.BACK_TO_SEARCH_BUTTON}")
    
    print("\nCommon Locators:")
    print(f"  HOME_LINK: {CommonLocators.HOME_LINK}")
    print(f"  LOGO: {CommonLocators.LOGO}")
    print(f"  LOADING_SPINNER: {CommonLocators.LOADING_SPINNER}")
    print(f"  SUBMIT_BUTTON: {CommonLocators.SUBMIT_BUTTON}")
    
    print("\n✓ All locators imported successfully!")
    
    # Test that locators are tuples with correct structure
    for locator_name, locator_value in [
        ("SEARCH_BOX", LandingPageLocators.SEARCH_BOX),
        ("SEARCH_ICON", LandingPageLocators.SEARCH_ICON),
        ("SEARCH_RESULTS_CONTAINER", SearchResultsPageLocators.SEARCH_RESULTS_CONTAINER)
    ]:
        assert isinstance(locator_value, tuple), f"{locator_name} should be a tuple"
        assert len(locator_value) == 2, f"{locator_value} should have 2 elements"
        print(f"  ✓ {locator_name} structure is correct")
    
    print("\n=== Locators Test Completed Successfully! ===")


if __name__ == "__main__":
    test_locators_import()
