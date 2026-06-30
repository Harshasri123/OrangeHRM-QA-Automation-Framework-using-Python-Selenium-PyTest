from utilities.config import BASE_URL, USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_login(setup):
    driver = setup

    login = LoginPage(driver).open(BASE_URL).login(USERNAME, PASSWORD)

    dashboard = DashboardPage(driver)
    assert dashboard.is_loaded(), "Dashboard should be loaded after successful login"

