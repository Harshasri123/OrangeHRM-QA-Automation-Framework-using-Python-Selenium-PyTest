# OrangeHRM-Automation-Framework

Selenium + Pytest automation framework for OrangeHRM demo site.

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run tests

```bash
pytest
```

HTML report will be generated at `reports/report.html`.

🧪 OrangeHRM Automation Framework (Python + Selenium + PyTest)
📌 Project Overview

This is a UI Test Automation Framework built using Python, Selenium WebDriver, and PyTest to automate the OrangeHRM web application.
It follows the Page Object Model (POM) design pattern for better maintainability and scalability.

🚀 Tech Stack
Python 3.x
Selenium WebDriver
PyTest
Page Object Model (POM)
HTML Reports (optional)
Git & GitHub
📂 Project Structure
OrangeHRM-Automation-Framework/
│
├── pages/              # Page Object classes
├── tests/             # Test scripts
├── utilities/         # Helper utilities (if any)
├── reports/          # Test execution reports
├── conftest.py       # PyTest fixtures
├── pytest.ini        # PyTest configuration
├── requirements.txt  # Dependencies
└── README.md
⚙️ Setup Instructions
1. Clone the repository
git clone https://github.com/Harshasri123/OrangeHRM-QA-Automation-Framework-using-Python-Selenium-PyTest.git
cd OrangeHRM-Automation-Framework
2. Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt
▶️ How to Run Tests

Run all tests:

pytest

Run specific test file:

pytest tests/test_login.py

Run with HTML report:

pytest --html=reports/report.html
🧪 Test Scenarios Covered
Login functionality
Logout functionality
Employee search
Add employee (PIM module)
📊 Reports

Test execution reports can be generated inside the reports/ folder.

🧠 Key Features
Page Object Model (POM) design
Reusable test components
PyTest fixtures for setup/teardown
Modular and scalable structure
Easy integration with CI/CD pipelines
⚠️ Known Issue
test_add_employee may fail due to dynamic UI locator timing (TimeoutException)
👩‍💻 Author

Harsha Sri Guduru
Software Engineer | QA Automation Enthusiast

⭐ Future Improvements
Add Allure reporting
Add CI/CD with GitHub Actions
Cross-browser testing
Parallel execution using pytest-xdist
📌 Note

This project is for learning and demonstrating QA automation skills using Selenium and Python.
