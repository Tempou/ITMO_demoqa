from pages.textbox_page import TextBox
from conftest import browser

def test_text_box(browser):
    textbox = TextBox(browser)

    textbox.visit()
    textbox.full_name.send_keys('Tim')
    textbox.current_address.send_keys('Spb')
    textbox.btn_submit.click()
    assert textbox.name_check.get_text() == 'Name:Tim'
    assert textbox.address_check.get_text() == 'Current Address :Spb'




