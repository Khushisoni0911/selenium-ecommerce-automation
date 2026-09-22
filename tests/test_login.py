import os
import pytest

from pages.login_page import LoginPage

@pytest.mark.regression
def test_invalid_login(driver):

    # Create LoginPage object
    login_page = LoginPage(driver)

    # Open login page
    login_page.open()

    # Perform login with invalid credentials
    login_page.login(
        "invaliduser@example.com",
        "wrongpassword123"
    )

    # Get error message
    error_message = login_page.get_error_message()

    print("Error Message:", error_message)

    # Verify error message
    assert error_message == "Your email or password is incorrect!"

    print("Invalid login test passed!")

@pytest.mark.smoke
def test_valid_login(driver):

    # Read credentials from environment variables
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    assert email is not None, \
        "TEST_EMAIL environment variable is not set"

    assert password is not None, \
        "TEST_PASSWORD environment variable is not set"

    # Create LoginPage object
    login_page = LoginPage(driver)

    # Open login page
    login_page.open()

    # Perform login
    login_page.login(email, password)

    # Verify successful login
    assert login_page.is_login_successful()

    # Get logged-in text
    logged_in_text = login_page.get_logged_in_text()

    print("Login verification:", logged_in_text)
    print("Valid login test passed!")

@pytest.mark.regression
def test_logout(driver):

    # Read credentials from environment variables
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    assert email is not None, \
        "TEST_EMAIL environment variable is not set"

    assert password is not None, \
        "TEST_PASSWORD environment variable is not set"

    # Create LoginPage object
    login_page = LoginPage(driver)

    # Open login page
    login_page.open()

    # Login with valid credentials
    login_page.login(email, password)

    # Verify login was successful
    assert login_page.is_login_successful()

    # Logout
    login_page.logout()

    # Verify user is redirected to login page
    assert "/login" in driver.current_url

    print("Logout test passed!")
    
@pytest.mark.regression
def test_empty_login_fields(driver):

    # Create LoginPage object
    login_page = LoginPage(driver)

    # Open login page
    login_page.open()

    # Verify email field is mandatory
    assert login_page.is_email_field_required()

    print("Empty login validation test passed!")    