#!/usr/bin/env python3
"""
First Selenium Python test script
Following the official documentation at: https://selenium-python.readthedocs.io/
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def setup():
    """Setup the browser and navigate to the website."""
    driver = webdriver.Chrome()
    driver.get("https://www.bstackdemo.com/")
    driver.maximize_window()
    return driver
    

def test_basic_selenium(driver):
        """Test the basic Selenium functionality."""
        # Get the page title
        title = driver.title
        print(f"Page title: {title}")
        assert "StackDemo" in driver.title
        
        # Find the search box and type something
        search_box = driver.find_element(By.XPATH, "//*[@placeholder='Search']")
        search_box.send_keys("Selenium Python")
        
        search_icon = driver.find_element(By.XPATH, "//*[text()='Search']")
        search_icon.click()

        # Get the new page title
        new_title = driver.title
        print(f"New page title: {new_title}")

def teardown(driver):
    """Teardown the browser and close the session."""
    driver.quit()

if __name__ == "__main__":
    driver = setup()
    test_basic_selenium(driver)
    teardown(driver)