import os
import unittest

from selenium import webdriver

from utilities.config_reader import ConfigReader


class BrowserTest(unittest.TestCase):

    def setUp(self):
        browser_name = ConfigReader.get_browser().lower()

        if browser_name == "chrome":
            options = webdriver.ChromeOptions()

            # GitHub Actions runs without a graphical display
            if os.getenv("CI"):
                options.add_argument("--headless=new")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--window-size=1920,1080")

            self.driver = webdriver.Chrome(options=options)

        else:
            raise ValueError(
                f"Unsupported browser: {browser_name}"
            )

        self.driver.maximize_window()

    def test_homepage_title(self):
        base_url = ConfigReader.get_base_url()

        self.driver.get(base_url)

        self.assertIn(
            "Automation Exercise",
            self.driver.title
        )

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()