# TODO - OrangeHRM-Automation-Framework

## Step 1 - Fix webdriver-manager PermissionError (WinError 5)
- Update `utilities/driver_factory.py` to avoid webdriver-manager OS detection that calls PowerShell/cmd.
- Prefer using an already-downloaded ChromeDriver path OR a different webdriver-manager configuration.

## Step 2 - Fix Login page verification failure
- `tests/test_login.py` / `pages/dashboard_page.py` selector not matching actual post-login dashboard.
- Update `DashboardPage.is_loaded()` locator(s).

## Step 3 - Fix PIM page element timeouts
- `pages/pim_page.py` locators for first/last name and buttons not matching actual page state.

## Step 4 - Screenshot hook on failure (optional but recommended)
- Update `conftest.py` to always capture screenshots when tests fail.

## Step 5 - Re-run `pytest -q` and validate
- Confirm tests pass and `reports/report.html` is generated.

