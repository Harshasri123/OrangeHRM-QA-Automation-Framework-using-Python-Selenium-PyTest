from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PimPage:
    """Page Object for PIM module."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # The 'Add' button inside the PIM employee list.
    # OrangeHRM 7.x commonly renders it as an 'Add' button in the header.
    ADD_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'oxd-button') and normalize-space()='Add']"
    )


    # These are commonly used fields in OrangeHRM add employee modal.
    FIRSTNAME = (By.NAME, "firstName")
    LASTNAME = (By.NAME, "lastName")

    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit'].oxd-button--secondary")

    def open_add_employee(self):
        # Navigation/menu selectors may vary; this method assumes you're already in PIM.
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()
        return self

    def add_employee(self, first_name, last_name):
        fn = self.wait.until(EC.visibility_of_element_located(self.FIRSTNAME))
        ln = self.wait.until(EC.visibility_of_element_located(self.LASTNAME))

        fn.clear(); fn.send_keys(first_name)
        ln.clear(); ln.send_keys(last_name)

        self.driver.find_element(*self.SAVE_BUTTON).click()
        return self

