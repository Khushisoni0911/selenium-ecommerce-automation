import pytest
import os
from datetime import datetime
from selenium import webdriver

from utilities.config_reader import ConfigReader


@pytest.fixture
def driver():

    # Read browser name from config.ini
    browser_name = ConfigReader.get_browser().lower()

    # Launch browser based on configuration
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError(
            f"Unsupported browser: {browser_name}"
        )

    # Maximize browser window
    driver.maximize_window()

    # Give browser to the test
    yield driver

    # Close browser after test
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Automatically capture a screenshot when a test fails."""

    outcome = yield
    report = outcome.get_result()

    # Capture screenshot only during the actual test execution
    if report.when == "call" and report.failed:

        # Get the driver used by the test
        driver = item.funcargs.get("driver")

        if driver:

            # Create screenshots directory if it does not exist
            os.makedirs("screenshots", exist_ok=True)

            # Create timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            # Create screenshot filename
            screenshot_name = (
                f"{item.name}_{timestamp}.png"
            )

            screenshot_path = os.path.join(
                "screenshots",
                screenshot_name
            )

            # Save screenshot
            driver.save_screenshot(screenshot_path)

# Add screenshot path to the PyTest report
            report.sections.append(
                (
                "Failure Screenshot",
                f"Screenshot saved at: {screenshot_path}"
               )
             )

            print(
              f"\nScreenshot saved: {screenshot_path}"
             )   