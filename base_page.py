from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def open(self):
        self.browser.get(self.link)

    def __init__(self, browser, link, timeout=20):
        self.browser = browser
        self.link = link
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, browser, link):
        try:
            self.browser.find_element(browser, link)
        except NoSuchElementException:
            return False
        return True
