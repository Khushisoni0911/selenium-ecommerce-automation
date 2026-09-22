# Selenium E-Commerce Automation Framework

A robust Selenium-based web automation framework developed using Python for testing an e-commerce application.

The framework automates major functionalities of the Automation Exercise website, including user login, logout, product search, invalid login validation, and data-driven product testing.

## Project Objective

The objective of this project is to design and implement a scalable Selenium automation framework using:

- Selenium WebDriver
- Python
- PyTest
- Unittest
- Page Object Model (POM)
- Data-Driven Testing using CSV
- Configuration Management
- Utility Classes
- Logging
- Screenshots on Test Failure
- HTML Reporting
- GitHub Actions CI/CD

## Application Under Test

Automation Exercise – E-Commerce Website

## Key Features

- Page Object Model based framework design
- PyTest fixtures for browser setup and teardown
- PyTest and Unittest test execution
- Valid and invalid login automation
- Logout functionality testing
- Product search automation
- Positive and negative search scenarios
- CSV-based data-driven testing
- Configuration management using `config.ini`
- Reusable utility classes
- Explicit waits for reliable element interaction
- Logging of test execution
- Automatic screenshots when tests fail
- HTML test reports
- Smoke and regression test markers
- Secure credential handling using environment variables
- Automated CI testing using GitHub Actions
- Headless Chrome execution in CI

## Test Coverage

The framework currently contains 11 automated test cases covering:

- Website launch and title validation
- Invalid login
- Valid login
- Logout
- Empty login field validation
- Product search
- Multiple product searches using CSV data
- Search for different products
- Search for a non-existing product
- Unittest-based browser validation

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Selenium WebDriver | Browser automation |
| PyTest | Primary testing framework |
| Unittest | Unit-style test framework |
| CSV | Data-driven test input |
| ConfigParser | Configuration management |
| pytest-html | HTML test reporting |
| Git | Version control |
| GitHub | Source code repository |
| GitHub Actions | CI/CD automation |
| Chrome | Test browser |
