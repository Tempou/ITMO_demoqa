from conftest import browser
from pages.alerts_page import AlertsPage
import time


#Задача 2
def test_timer(browser):
    alert_page = AlertsPage(browser)

    alert_page.visit()
    assert not alert_page.alert()

    alert_page.btn_timer.click_force()
    time.sleep(10)
    assert alert_page.alert()
    assert alert_page.alert().text == 'This alert appeared after 5 seconds'