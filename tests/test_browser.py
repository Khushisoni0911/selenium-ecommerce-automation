import pytest
from utilities.logger import Logger


logger = Logger.get_logger(__name__)

@pytest.mark.smoke
def test_open_website(driver):


    logger.info("Opening Automation Exercise website")

    driver.get("https://automationexercise.com/")

    logger.info(f"Page title: {driver.title}")

    assert "Automation Exercise" in driver.title
    # assert "WRONG TITLE" in driver.title

    logger.info("Browser test passed successfully")