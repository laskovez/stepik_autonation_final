import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: en ot ru")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    browser = None
    options = Options()
    if browser_language == "en":
        print("\nstart en language for test..")
        options.add_experimental_option('prefs', {'intl.accept_languages': "en"})
        browser = webdriver.Chrome(options=options)
    elif browser_language == "ru":
        print("\nstart ru language for test..")
        options.add_experimental_option('prefs', {'intl.accept_languages': "ru"})
        browser = webdriver.Chrome(options=options)

    yield browser
    print("\nquit browser...")
    browser.quit()
