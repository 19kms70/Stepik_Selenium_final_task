import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    """
    для запуска :
        pytest -s -v --tb=short --browser_name=firefox --language=en test_conftest.py
        pytest -s -v --tb=short --browser_name=chrome --language=en test_conftest.py
    по умолчанию броузер 'chrome' и язык 'en'
        pytest -s -v --tb=line test_main_page.py
    """

    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru or en-gb (for example)")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print(f"{language=}")
    if not language:
        raise pytest.UsageError("--language should be defined ( ru,en for example )")
    else:
        print(f"\nstart chrome browser with {language} language")


    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)


    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        from selenium.webdriver.firefox.options import Options
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        browser = webdriver.Firefox(options=options,firefox_profile=fp)


    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

