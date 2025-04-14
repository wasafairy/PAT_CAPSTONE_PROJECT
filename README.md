SauceDemo Automation Testing with Selenium, Python & Pytest

This project is an automation testing framework for [SauceDemo](https://www.saucedemo.com), built using **Selenium WebDriver**, **Python**, **Pytest**, and executed via **PyCharm**.
This project is done by using python oops and exceptional handling.
Pytest is used to generate html based reports for automation testing.


PROJECT STRUCTURE
saucedemo_automation/
|
|-- pages/
    |---login_page.py              # Page class for Login
    |---inventory_page.py          # Page class for Inventory
    |---cart_page.py               # Page class for Cart
    |---checkout_page.py           # Page class for Checkout
|
|-- tests/
    |---test_login.py              # Test-case 1 & 2
    |---test_logout.py             # Test-case 3
    |---test_cart.py               # Test-case 4, 5, 6, 7
    |---test_checkout.py           # Test-case 8
|
|-- utils/
    |---base_test.py               # Base class for common setup/teardown
|--reports/
    |---pytest-html-reports/
|
|--requirements.txt
|--README.md
|

RUNNING TESTS

FROM COMMAND LINE:
pytest

TO RUN A SPECIFIC TEST:
pytest tests/test_login.py

TO GENERATE AN HTML REPORT:
pytest --html=report.html

FROM PYCHARM
Right click the tests/ folder or any test file
Select Run 'pytest in tests'
The results are excecuted in PyCharm’s test runner tab

TO SEE CONSOLE print() OUTPUT 
use pytest -s


CONTRIBUTED BY
 KANISHKA S
 

