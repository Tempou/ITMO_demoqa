from pages.textbox_page import TextBox
from conftest import browser

def test_placeholder(browser):
    textbox = TextBox(browser)

    textbox.visit()
    assert textbox.full_name.get_dom_attribute('id') == 'userName'