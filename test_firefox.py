#!/usr/bin/env python3
"""
Test script to demonstrate Firefox driver behavior
This will show the difference between Selenium Manager and manual driver installation
"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

def test_firefox_without_driver():
    """Test Firefox WebDriver to see if we get driver errors."""
    print("Testing Firefox WebDriver...")
    
    try:
        # Try to create Firefox driver without specifying a driver path
        # This will rely on Selenium Manager to find/download the driver
        print("Attempting to create Firefox driver...")
        driver = webdriver.Firefox()
        
        print("Firefox driver created successfully!")
        print("Navigating to a test page...")
        
        driver.get("https://www.example.com")
        print(f"Page title: {driver.title}")
        
        driver.quit()
        print("Firefox test completed successfully!")
        
    except Exception as e:
        print(f"Error occurred: {type(e).__name__}: {e}")
        print("\nThis error would typically occur in older Selenium versions")
        print("when drivers weren't automatically managed.")

def test_firefox_with_manual_service():
    """Test Firefox with manual service specification."""
    print("\n" + "="*50)
    print("Testing Firefox with manual service specification...")
    
    try:
        # This approach would be used in older Selenium versions
        # where you manually specify the driver path
        print("Attempting to create Firefox driver with manual service...")
        
        # Note: In older versions, you'd need to specify the path like:
        # service = Service('/path/to/geckodriver')
        # driver = webdriver.Firefox(service=service)
        
        # For now, let's just show the concept
        print("This would require manually downloading geckodriver from:")
        print("https://github.com/mozilla/geckodriver/releases")
        print("And placing it in your PATH or specifying the full path.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_firefox_without_driver()
    test_firefox_with_manual_service()
