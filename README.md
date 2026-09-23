# Selenium E-Commerce Automation Framework

A Selenium automation framework built using **Python, PyTest, Unittest, and Page Object Model (POM)** to test common workflows of an e-commerce website.

The project uses **Automation Exercise** as the application under test and covers login, logout, product search, data-driven testing, reporting, and CI/CD.

## Features

- Selenium WebDriver with Python
- Page Object Model (POM)
- PyTest and Unittest
- Valid and invalid login testing
- Product search testing
- CSV-based data-driven testing
- Configuration management using `config.ini`
- Explicit waits
- Logging
- Screenshots on test failure
- HTML test reports
- Smoke and regression testing
- GitHub Actions CI
- Secure credentials using environment variables

## Project Structure

```text
selenium-ecommerce-automation/
├── .github/workflows/     # GitHub Actions
├── config/                # Configuration
├── pages/                 # Page Object classes
├── testdata/              # CSV test data
├── tests/                 # Test cases
├── utilities/             # Reusable utilities
├── reports/               # HTML reports
├── screenshots/           # Failure screenshots
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Test Scenarios

The framework currently contains **11 automated tests**, including:

- Website launch validation
- Valid and invalid login
- Logout
- Empty login fields
- Product search
- CSV-driven product search
- Different and non-existing product searches
- Unittest browser validation

## Setup

Clone the repository and install the dependencies:

```bash
git clone https://github.com/Khushisoni0911/selenium-ecommerce-automation.git
cd selenium-ecommerce-automation

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

For valid login tests, set the test account credentials as environment variables:

```bash
export TEST_EMAIL="your_test_email"
export TEST_PASSWORD="your_test_password"
```

Credentials are not stored in the source code.

## Running Tests

Run all tests:

```bash
pytest tests/ -v
```

Run only smoke or regression tests:

```bash
pytest tests/ -m smoke -v
pytest tests/ -m regression -v
```

Generate an HTML report:

```bash
pytest tests/ -v --html=reports/report.html --self-contained-html
```

If a test fails, the framework automatically saves a screenshot inside the `screenshots/` folder.

## CI/CD

GitHub Actions runs the Selenium test suite automatically on pushes and pull requests to the `main` branch.

Chrome runs in **headless mode** in the CI environment, while login credentials are securely accessed through GitHub Repository Secrets.

## Tech Stack

**Python | Selenium | PyTest | Unittest | POM | CSV | Git | GitHub Actions**

## Author

**Khushi Soni**  
B.Tech – Information Technology  
Institute of Engineering & Management, Kolkata
