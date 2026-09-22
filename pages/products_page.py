from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.config_reader import ConfigReader

class ProductsPage:

    # URL
    PRODUCTS_URL = ConfigReader.get_base_url() + "/products"
    

    # Locators
    SEARCH_INPUT = (
        By.ID,
        "search_product"
    )

    SEARCH_BUTTON = (
        By.ID,
        "submit_search"
    )

    SEARCHED_PRODUCTS_HEADING = (
        By.XPATH,
        "//h2[contains(text(),'Searched Products')]"
    )

    # PRODUCT_NAME = (
    #     By.XPATH,
    #     "//p[contains(text(),'Blue Top')]"
    # )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
             driver,
             ConfigReader.get_explicit_wait()
                  )

    def open(self):
        """Open the products page."""
        self.driver.get(self.PRODUCTS_URL)


    def search_product(self, product_name):
        """Search for a product."""

        # Wait for search box
        search_box = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )

        # Clear existing text
        search_box.clear()

        # Enter product name
        search_box.send_keys(product_name)

        # Wait for search button and click it
        search_button = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )

        search_button.click()


    def is_searched_products_heading_displayed(self):
        """Check whether Searched Products heading is displayed."""

        heading = self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCHED_PRODUCTS_HEADING
            )
        )

        return heading.is_displayed()


    def is_product_displayed(self, product_name):
        """Check whether the searched product is displayed."""

        # Find all product names currently displayed
        products = self.driver.find_elements(
            By.CSS_SELECTOR,
            ".productinfo p"
        )

        # Normalize expected product name
        expected_name = " ".join(product_name.split())

        # Check each displayed product
        for product in products:

            # Normalize website product name
            actual_name = " ".join(product.text.split())

            if actual_name == expected_name:
                return True

        # Product was not found
        return False   
    
    def get_all_product_names(self):
        """Return all visible product names from search results."""

        products = self.driver.find_elements(
            By.CSS_SELECTOR,
            ".productinfo p"
        )

        return [
            product.text
            for product in products
            if product.text.strip()
        ]   