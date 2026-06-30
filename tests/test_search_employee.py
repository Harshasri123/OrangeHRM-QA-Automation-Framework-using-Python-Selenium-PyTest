from utilities.config import BASE_URL, USERNAME, PASSWORD
from pages.login_page import LoginPage


def test_search_employee(setup):
    driver = setup

    LoginPage(driver).open(BASE_URL).login(USERNAME, PASSWORD)

    # Minimal scaffold: actual PIM search locators are not implemented in this template.
    # Add search page object / locators as needed.
    assert True

