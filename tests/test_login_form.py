from components.components import WebElement
from pages.form_page import FormPage
from conftest import browser
import time

def test_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()

    assert not form_page.modal_dialog.exists()
    time.sleep(2)

    form_page.first_name.send_keys("Tim")
    form_page.last_name.send_keys("Capello")
    form_page.user_email.send_keys("123timcapello@gmail.com")
    form_page.gender_radio_1.click()
    form_page.user_email.send_keys("88005553535")
    time.sleep(2)

    form_page.btn_submit.click()
    time.sleep(2)


