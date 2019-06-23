from selenium.webdriver.common.by import By

from page.basepage import BasePageObject

class Testbook(BasePageObject):
    _search = (By.NAME,"search_text")
    _search_text  = "python"
    _clicksearch = (By.CLASS_NAME,"inp-btn")
    _bookname = (By.CLASS_NAME,"title-text")

    def __init__(self):
        BasePageObject.__init__(self)
    def to_search(self):
        return self.extend_find_element(Testbook._search)
    def send_value(self):
        self.set_value(self.to_search(),Testbook._search_text)
        return self
    def click_search(self):
        return self.extend_find_element(Testbook._clicksearch)
    def book_result(self):
        self.click_element(self.click_search())
    def get_bookname(self):
        return self.get_element_text(self.extend_find_elements(Testbook._bookname)[1])


    def find_book(self):
        self.to_search()
        self.send_value().click_search()
        self.book_result()
        return self
    def close_chrome(self):
        self.driver.quit()

