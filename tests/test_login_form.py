from pages.form_page import FormPage
from conftest import browser
import time


def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exists()
    time.sleep(2)
    form_page.first_name.send_keys("tim")
    form_page.last_name.send_keys("capello")
    form_page.user_email.send_keys("test@ttt.tt")
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys("18381388311")
    form_page.hobbies.click_force()
    form_page.current_adress.send_keys("SPB")
    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(2)

    assert form_page.modal_dialog.exists()
    form_page.btn_close_modal.click_force()


def test_state_city(browser):
    form_page = FormPage(browser)

    form_page.visit()
    form_page.state.click()
    time.sleep(2)
    form_page.state_ncr.click()
    form_page.city.click()
    time.sleep(2)
    form_page.city_noida.click()
    time.sleep(2)


def test_state_city_keys(browser):
    form_page = FormPage(browser)
    form_page.visit()



