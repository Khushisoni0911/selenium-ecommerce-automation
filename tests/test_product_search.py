import os
import pytest

from pages.products_page import ProductsPage
from utilities.csv_reader import CSVReader

def load_product_data():
    """Load product names using the CSVReader utility."""

    file_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "testdata",
        "products.csv"
    )

    return CSVReader.read_column(
        file_path,
        "product_name"
    )
@pytest.mark.regression
@pytest.mark.parametrize("product_name", load_product_data())
def test_product_search_from_csv(driver, product_name):

    # Create ProductsPage object
    products_page = ProductsPage(driver)

    # Open products page
    products_page.open()

    # Search using product name received from CSV
    products_page.search_product(product_name)

    # Verify searched products heading
    assert products_page.is_searched_products_heading_displayed()

    # Verify product is displayed
    assert products_page.is_product_displayed(product_name)

    print(f"CSV Test Passed for product: {product_name}")

@pytest.mark.smoke
def test_product_search(driver):

    # Test data
    product_name = "Blue Top"

    # Create ProductsPage object
    products_page = ProductsPage(driver)

    # Open products page
    products_page.open()

    print("Current URL:", driver.current_url)
    print("Page Title:", driver.title)

    # Search for product
    products_page.search_product(product_name)

    # Verify searched products heading
    assert products_page.is_searched_products_heading_displayed()

    # Verify searched product
    assert products_page.is_product_displayed(product_name)

    print(f"Product '{product_name}' found successfully!")
    print("Product search test passed!")

@pytest.mark.regression
def test_search_different_product(driver):

    # Test data
    product_name = "Sleeveless Dress"

    # Create ProductsPage object
    products_page = ProductsPage(driver)

    # Open products page
    products_page.open()

    # Search for another product
    products_page.search_product(product_name)

    # Verify searched products heading
    assert products_page.is_searched_products_heading_displayed()

    # Verify searched product
    assert products_page.is_product_displayed(product_name)

    print(f"Product '{product_name}' found successfully!")
    print("Different product search test passed!")

@pytest.mark.regression
def test_search_non_existing_product(driver):

    # Test data - intentionally invalid product
    product_name = "XYZ123NOTEXIST"

    # Create ProductsPage object
    products_page = ProductsPage(driver)

    # Open products page
    products_page.open()

    # Search for non-existing product
    products_page.search_product(product_name)

    # Verify search results section appears
    assert products_page.is_searched_products_heading_displayed()

    # Verify the product is NOT displayed
    assert not products_page.is_product_displayed(product_name)

    print(f"Product '{product_name}' was not found, as expected.")
    print("Non-existing product search test passed!")    