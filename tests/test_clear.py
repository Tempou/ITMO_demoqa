from pages.textbox_page import TextBox
from conftest import browser
import time

def test_clear(browser):
    textbox = TextBox(browser)

    textbox.visit()
    textbox.full_name.send_keys("12322323")
    time.sleep(2)
    textbox.full_name.clear()
    time.sleep(2)
    assert textbox.full_name.get_text() == ''