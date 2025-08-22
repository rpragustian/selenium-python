from selenium.webdriver.common.by import By


class SearchResultsPageLocators:
    """Locators for the search results page elements."""
    
    # Search results container
    SEARCH_RESULTS_CONTAINER = (By.CLASS_NAME, "search-results")
    SEARCH_RESULTS_LIST = (By.CLASS_NAME, "result-item")
    
    # Result item elements
    RESULT_TITLE = (By.CLASS_NAME, "result-title")
    RESULT_DESCRIPTION = (By.CLASS_NAME, "result-description")
    RESULT_LINK = (By.CLASS_NAME, "result-link")
    RESULT_IMAGE = (By.CLASS_NAME, "result-image")
    
    # Navigation and messages
    NO_RESULTS_MESSAGE = (By.CLASS_NAME, "no-results")
    BACK_TO_SEARCH_BUTTON = (By.CLASS_NAME, "back-to-search")
    SEARCH_AGAIN_BUTTON = (By.CLASS_NAME, "search-again")
    
    # Pagination (if applicable)
    NEXT_PAGE_BUTTON = (By.CLASS_NAME, "next-page")
    PREVIOUS_PAGE_BUTTON = (By.CLASS_NAME, "previous-page")
    PAGE_NUMBER = (By.CLASS_NAME, "page-number")
    PAGE_NAVIGATION = (By.CLASS_NAME, "page-navigation")
    
    # Filters and sorting
    FILTER_SIDEBAR = (By.CLASS_NAME, "filter-sidebar")
    SORT_DROPDOWN = (By.CLASS_NAME, "sort-dropdown")
    VIEW_TOGGLE = (By.CLASS_NAME, "view-toggle")
