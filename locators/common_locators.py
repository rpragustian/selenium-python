from selenium.webdriver.common.by import By


class CommonLocators:
    """Common locators that might be used across multiple pages."""
    
    # Common navigation elements
    HOME_LINK = (By.CLASS_NAME, "home-link")
    LOGO = (By.CLASS_NAME, "logo")
    MAIN_NAVIGATION = (By.CLASS_NAME, "main-navigation")
    BREADCRUMB = (By.CLASS_NAME, "breadcrumb")
    
    # Common UI elements
    LOADING_SPINNER = (By.CLASS_NAME, "loading-spinner")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "success-message")
    INFO_MESSAGE = (By.CLASS_NAME, "info-message")
    
    # Common buttons
    SUBMIT_BUTTON = (By.CLASS_NAME, "submit-button")
    CANCEL_BUTTON = (By.CLASS_NAME, "cancel-button")
    CLOSE_BUTTON = (By.CLASS_NAME, "close-button")
    BACK_BUTTON = (By.CLASS_NAME, "back-button")
    
    # Common form elements
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    EMAIL_FIELD = (By.ID, "email")
    SUBMIT_FORM = (By.CLASS_NAME, "submit-form")
    
    # Common page elements
    PAGE_HEADER = (By.TAG_NAME, "h1")
    PAGE_CONTENT = (By.CLASS_NAME, "page-content")
    SIDEBAR = (By.CLASS_NAME, "sidebar")
    FOOTER = (By.TAG_NAME, "footer")
    
    # Common actions
    LOGIN_BUTTON = (By.CLASS_NAME, "login-button")
    LOGOUT_BUTTON = (By.CLASS_NAME, "logout-button")
    PROFILE_BUTTON = (By.CLASS_NAME, "profile-button")
    SETTINGS_BUTTON = (By.CLASS_NAME, "settings-button")
