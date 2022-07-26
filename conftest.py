import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(7)
    browser.get('chrome://settings/clearBrowserData')
    browser.find_element_by_xpath('//settings-ui').send_keys(Keys.ENTER)
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('useAutomationExtension', False)
    # options.add_argument("--start-maximized")
    # options.add_argument('window-size=1200,940')
    # browser = webdriver.Chrome(chrome_options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
