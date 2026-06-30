from utilities.config import BASE_URL, USERNAME, PASSWORD
from pages.login_page import LoginPage


def test_logout(setup):
    driver = setup

    LoginPage(driver).open(BASE_URL).login(USERNAME, PASSWORD)

    # Logout selectors can vary; attempt the typical OrangeHRM user menu flow.
    user_menu = driver.find_element("css selector", "i.oxd-icon.bi-caret-down-fill")
    user_menu.click()

    logout = driver.find_element("xpath", "//a[contains(.,'Logout')]")
    logout.click()

    # If logout succeeded, the login form should be present.
    assert driver.find_elements("name", "username"), "Login page should be visible after logout"

