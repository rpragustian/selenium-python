#!/usr/bin/env python3
"""
Test script demonstrating the Page Objects design pattern.
This script shows how to use page objects to make tests more maintainable
and readable.
"""

from selenium import webdriver
from pages.landing_page import LandingPage


def setup():
    """Setup the browser and return the webdriver instance."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def test_landing_page_with_page_objects(driver):
    """Test the landing page using the Page Objects pattern."""
    # Create a landing page object
    landing_page = LandingPage(driver)
    
    # Load the landing page
    print("Loading landing page...")
    landing_page.load()
    
    # Verify the page loaded correctly
    print("Verifying page loaded...")
    assert landing_page.verify_page_loaded()
    
    # Get page information
    print(f"Page title: {landing_page.get_page_title()}")
    print(f"Current URL: {landing_page.get_current_url()}")
    
    # Check page elements status
    elements_status = landing_page.get_page_elements_status()
    print("Page elements status:")
    for element, status in elements_status.items():
        print(f"  {element}: {status}")
    
    # Test search functionality
    print("\nTesting search functionality...")
    search_term = "Selenium Python"
    landing_page.search_for(search_term)
    
    # Verify search was performed
    search_box_text = landing_page.get_search_box_text()
    print(f"Search box contains: '{search_box_text}'")
    
    # Get the new page title after search
    new_title = landing_page.get_page_title()
    print(f"New page title after search: {new_title}")
    
    print("\nAll tests passed successfully!")


def teardown(driver):
    """Teardown the browser and close the session."""
    driver.quit()


if __name__ == "__main__":
    driver = setup()
    try:
        test_landing_page_with_page_objects(driver)
    finally:
        teardown(driver)
