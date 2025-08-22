from selenium.webdriver.common.by import By


class LandingPageLocators:
    """Locators for the landing page elements."""
    
    # Search functionality
    SEARCH_BOX = (By.XPATH, "//*[@placeholder='Search']")
    SEARCH_ICON = (By.XPATH, "//*[text()='Search']")
    
    # Page structure elements
    PAGE_TITLE = (By.TAG_NAME, "title")
    HEADER = (By.TAG_NAME, "header")
    MAIN_CONTENT = (By.TAG_NAME, "main")
    FOOTER = (By.TAG_NAME, "footer")
    
    # Additional UI elements
    NAVIGATION_MENU = (By.CLASS_NAME, "nav-menu")
    LOGO = (By.CLASS_NAME, "logo")
    USER_MENU = (By.CLASS_NAME, "user-menu")
