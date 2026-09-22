from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.config_reader import ConfigReader

class LoginPage:

    # URL
    LOGIN_URL = ConfigReader.get_base_url() + "/login"

    # Locators
    EMAIL_INPUT = (
        By.CSS_SELECTOR,
        ".login-form input[name='email']"
    )

    PASSWORD_INPUT = (
        By.CSS_SELECTOR,
        ".login-form input[name='password']"
    )

    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        ".login-form button[type='submit']"
    )

    ERROR_MESSAGE = (
        By.XPATH,
        "//p[contains(text(),'Your email or password is incorrect!')]"
    )

    LOGGED_IN_TEXT = (
        By.XPATH,
        "//a[contains(.,'Logged in as')]"
    )
    LOGOUT_LINK = (
    By.XPATH,
    "//a[contains(.,'Logout')]"
    )

    def __init__(self, driver):
     self.driver = driver

     self.wait = WebDriverWait(
        driver,
        ConfigReader.get_explicit_wait()
    )


    def open(self):
        """Open the login page."""
        self.driver.get(self.LOGIN_URL)


    def enter_email(self, email):
        """Enter email in the login email field."""
        email_field = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )
        email_field.clear()
        email_field.send_keys(email)


    def enter_password(self, password):
        """Enter password in the password field."""
        password_field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        password_field.clear()
        password_field.send_keys(password)


    def click_login(self):
        """Click the Login button."""
        login_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        login_button.click()
    
    def login(self, email, password):
        """Perform the complete login action."""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login() 
    def get_error_message(self):
        """Return the invalid login error message."""
        error_message = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return error_message.text


    def is_login_successful(self):
        """Check whether the user is successfully logged in."""
        logged_in_element = self.wait.until(
            EC.visibility_of_element_located(self.LOGGED_IN_TEXT)
        )
        return logged_in_element.is_displayed()


    def get_logged_in_text(self):
        """Return the logged-in user text."""
        logged_in_element = self.wait.until(
            EC.visibility_of_element_located(self.LOGGED_IN_TEXT)
        )
        return logged_in_element.text  

    def logout(self):
        """Logout the currently logged-in user."""

        logout_link = self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT_LINK)
        )

        logout_link.click()  

    def is_email_field_required(self):
        """Check whether the email field is required."""

        email_field = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )

        return email_field.get_attribute("required") is not None                      