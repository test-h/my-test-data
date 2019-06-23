from page.bookepage import Testbook
import pytest
class Test_book:
    def test_bookvisable(self):
        testbook = Testbook()
        testbook.find_book()
        text = testbook.get_bookname()
        testbook.close_chrome()
        assert text == "Python编程快速上手 : 让繁琐工作自动化"
