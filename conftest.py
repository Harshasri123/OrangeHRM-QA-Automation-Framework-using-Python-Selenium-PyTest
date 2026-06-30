import pytest

from utilities.driver_factory import get_driver


@pytest.fixture
def setup():
    driver = get_driver()

    yield driver

    driver.quit()

