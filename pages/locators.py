from selenium.webdriver.common.by import By


class LandingPageLocators(object):
    """A class for landing page locators. All landing page locators should come here"""
    
    # Search functionality
    SEARCH_BOX = (By.XPATH, "//*[@placeholder='Search']")
    SEARCH_ICON = (By.XPATH, "//*[text()='Search']")
    
    # Page structure elements
    PAGE_TITLE = (By.TAG_NAME, "title")
    HEADER = (By.TAG_NAME, "header")
    MAIN_CONTENT = (By.TAG_NAME, "main")
    FOOTER = (By.TAG_NAME, "footer")


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    
    # Search results container
    SEARCH_RESULTS_CONTAINER = (By.CLASS_NAME, "search-results")
    SEARCH_RESULTS_LIST = (By.CLASS_NAME, "result-item")
    
    # Result item elements
    RESULT_TITLE = (By.CLASS_NAME, "result-title")
    RESULT_DESCRIPTION = (By.CLASS_NAME, "result-description")
    RESULT_LINK = (By.CLASS_NAME, "result-link")
    
    # Navigation and messages
    NO_RESULTS_MESSAGE = (By.CLASS_NAME, "no-results")
    BACK_TO_SEARCH_BUTTON = (By.CLASS_NAME, "back-to-search")
    
    # Pagination (if applicable)
    NEXT_PAGE_BUTTON = (By.CLASS_NAME, "next-page")
    PREVIOUS_PAGE_BUTTON = (By.CLASS_NAME, "previous-page")
    PAGE_NUMBER = (By.CLASS_NAME, "page-number")


class CommonLocators(object):
    """A class for common locators that might be used across multiple pages"""
    
    # Common navigation elements
    HOME_LINK = (By.CLASS_NAME, "home-link")
    LOGO = (By.CLASS_NAME, "logo")
    
    # Common UI elements
    LOADING_SPINNER = (By.CLASS_NAME, "loading-spinner")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "success-message")
    
    # Common buttons
    SUBMIT_BUTTON = (By.CLASS_NAME, "submit-button")
    CANCEL_BUTTON = (By.CLASS_NAME, "cancel-button")
    CLOSE_BUTTON = (By.CLASS_NAME, "close-button")