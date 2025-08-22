#!/usr/bin/env python3
"""
Comprehensive test demonstrating Page Objects workflow.
This test shows how multiple page objects can work together
to create a complete user journey test.
"""

from selenium import webdriver
from pages.landing_page import LandingPage
from pages.search_results_page import SearchResultsPage


def setup():
    """Setup the browser and return the webdriver instance."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def test_complete_search_workflow(driver):
    """Test the complete search workflow using multiple page objects."""
    print("=== Starting Complete Search Workflow Test ===\n")
    
    # Step 1: Load the landing page
    print("Step 1: Loading landing page...")
    landing_page = LandingPage(driver)
    landing_page.load()
    
    # Verify landing page loaded
    assert landing_page.verify_page_loaded()
    print(f"✓ Landing page loaded successfully")
    print(f"  Title: {landing_page.get_page_title()}")
    print(f"  URL: {landing_page.get_current_url()}")
    
    # Check landing page elements
    landing_status = landing_page.get_page_elements_status()
    print(f"  Search box visible: {landing_status['search_box_visible']}")
    print(f"  Search icon visible: {landing_status['search_icon_visible']}")
    
    # Step 2: Perform a search
    print("\nStep 2: Performing search...")
    search_term = "Selenium Python"
    landing_page.search_for(search_term)
    print(f"✓ Search performed for: '{search_term}'")
    
    # Step 3: Handle search results page
    print("\nStep 3: Handling search results page...")
    search_results_page = SearchResultsPage(driver)
    
    # Wait for results to load
    results_loaded = search_results_page.wait_for_results_to_load()
    if results_loaded:
        print("✓ Search results loaded successfully")
        
        # Get results information
        results_count = search_results_page.get_results_count()
        print(f"  Number of results: {results_count}")
        
        if results_count > 0:
            result_titles = search_results_page.get_result_titles()
            print(f"  First few result titles:")
            for i, title in enumerate(result_titles[:3], 1):
                print(f"    {i}. {title}")
            
            # Click on first result
            print("\n  Clicking on first result...")
            if search_results_page.click_first_result():
                print("✓ First result clicked successfully")
            else:
                print("✗ Failed to click first result")
        else:
            print("  No search results found")
    else:
        print("✗ Search results failed to load")
        
        # Check if no results message is displayed
        if search_results_page.is_no_results_displayed():
            print("  'No results' message is displayed")
    
    # Step 4: Get final page information
    print("\nStep 4: Final page information...")
    final_url = search_results_page.get_current_url()
    final_title = search_results_page.get_title()
    print(f"  Final URL: {final_url}")
    print(f"  Final title: {final_title}")
    
    print("\n=== Test Completed Successfully! ===")


def test_page_object_reusability(driver):
    """Test the reusability of page objects."""
    print("\n=== Testing Page Object Reusability ===\n")
    
    # Create landing page object
    landing_page = LandingPage(driver)
    
    # Navigate to landing page
    landing_page.navigate_to("https://www.bstackdemo.com/")
    
    # Test multiple search operations
    search_terms = ["Python", "Selenium", "Testing"]
    
    for term in search_terms:
        print(f"Testing search for: '{term}'")
        
        # Clear previous search
        landing_page.clear_search()
        
        # Perform new search
        landing_page.search_for(term)
        
        # Verify search was performed
        search_box_text = landing_page.get_search_box_text()
        print(f"  Search box contains: '{search_box_text}'")
        
        # Small delay to see the results
        import time
        time.sleep(1)
    
    print("✓ Page object reusability test completed")


def teardown(driver):
    """Teardown the browser and close the session."""
    driver.quit()


if __name__ == "__main__":
    driver = setup()
    try:
        # Run the complete workflow test
        test_complete_search_workflow(driver)
        
        # Run the reusability test
        test_page_object_reusability(driver)
        
    finally:
        teardown(driver)
