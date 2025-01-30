from conftest import browser
from pages.alerts_page import AlertsPage
import time

def test_alerts(browser):
    alert_page = AlertsPage(browser)

    alert_page.visit()
    assert not alert_page.alert()

    alert_page.btn_alert.click()
    time.sleep(2)
    assert alert_page.alert()


def test_alert_text(browser):
    alert_page = AlertsPage(browser)

    alert_page.visit()
    alert_page.btn_alert.click()
    time.sleep(2)
    assert alert_page.alert().text == 'You clicked a button'

    alert_page.alert().accept()
    assert not alert_page.alert()


def test_confirm(browser):
    alert_page = AlertsPage(browser)

    alert_page.visit()
    alert_page.btn_confirm.click()
    time.sleep(2)
    alert_page.alert().dismiss()
    time.sleep(2)

    assert alert_page.confirm_result.get_text() == 'You selected Cancel'

def test_prompt(browser):
    alert_page = AlertsPage(browser)
    # name = 'Tim'

    alert_page.visit()
    alert_page.btn_prompt.click()
    time.sleep(2)

    alert_page.alert().send_keys('Tim')
    alert_page.alert().accept()

    assert alert_page.prompt_result.get_text() == 'You entered Tim'
    # assert alert_page.prompt_result.get_text() == f'You entered { name }'
    time.sleep(2)



