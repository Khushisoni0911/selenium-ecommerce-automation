import unittest
from selenium import webdriver

from utilities.config_reader import ConfigReader


class BrowserTest(unittest.TestCase):

    def setUp(self):
        """Run before every test."""

        browser_name = ConfigReader.get_browser().lower()

        if browser_name == "chrome":
            self.driver = webdriver.Chrome()
        else:
            raise ValueError(
                f"Unsupported browser: {browser_name}"
            )

        self.driver.maximize_window()


    def test_homepage_title(self):
        """Verify the homepage title."""

        base_url = ConfigReader.get_base_url()

        self.driver.get(base_url)

        self.assertIn(
            "Automation Exercise",
            self.driver.title
        )


    def tearDown(self):
        """Run after every test."""

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()