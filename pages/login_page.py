from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object for OrangeHRM Login."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Locators based on the OrangeHRM demo login page structure.
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def open(self, base_url):
        self.driver.get(base_url)
        return self

    def login(self, username, password):
        username_el = self.wait.until(EC.visibility_of_element_located(self.USERNAME))
        password_el = self.wait.until(EC.visibility_of_element_located(self.PASSWORD))

        username_el.clear()
        username_el.send_keys(username)

        password_el.clear()
        password_el.send_keys(password)

        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self

