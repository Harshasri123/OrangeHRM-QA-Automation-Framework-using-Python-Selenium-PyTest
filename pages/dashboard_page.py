from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    """Page Object for OrangeHRM Dashboard/Home after login."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # More reliable OrangeHRM 7.x dashboard check.
    # OrangeHRM dashboard header: <h6>Dashboard</h6>
    DASHBOARD_TITLE = (By.XPATH, "//h6[normalize-space()='Dashboard']")

    def is_loaded(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.DASHBOARD_TITLE))
            return True
        except Exception:
            return False


