import os
from datetime import datetime

import pytest
from selenium import webdriver

from utilities.config_reader import ConfigReader

@pytest.fixture
def driver():
    browser_name = ConfigReader.get_browser().lower()

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()

        # GitHub Actions runs without a graphical display
        if os.getenv("CI"):
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)

    else:
        raise ValueError(
            f"Unsupported browser: {browser_name}"
        )

    driver.maximize_window()

    yield driver

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