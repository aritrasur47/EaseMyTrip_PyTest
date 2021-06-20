import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def browser_setup(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome(
            executable_path="F:\\Users\\maila\\PycharmProjects\\python_testing\\driver\\chromedriver_win32\\chromedriver.exe")
    else:
        driver = webdriver.Firefox(
            executable_path="F:\\Users\\maila\\PycharmProjects\\python_testing\\driver\\geckodriver_win64\\geckodriver.exe")

    driver.get("https://www.easemytrip.com/flights.html")
    driver.implicitly_wait(8)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
