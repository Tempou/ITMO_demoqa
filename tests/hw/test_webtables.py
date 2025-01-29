from pages.webtables_page import WebTables
from conftest import browser
import time

def test_webtables(browser):
    webtable = WebTables(browser)

    webtable.visit()
    webtable.btn_add.click()
    time.sleep(2)
    assert not webtable.regformvalid.get_dom_attribute('class') == 'was-validated'
    webtable.btn_submit.click()
    assert webtable.regformvalid.get_dom_attribute('class') == 'was-validated'
    webtable.btn_close.click()

    webtable.btn_add.click()
    webtable.first_name.send_keys("Tim")
    webtable.last_name.send_keys("Capello")
    webtable.email.send_keys("ttttt@ttt.com")
    webtable.age.send_keys("22")
    webtable.salary.send_keys("199831")
    webtable.department.send_keys("Department")
    webtable.btn_submit.click()
    time.sleep(1)
    assert webtable.newstr.exists()

    webtable.btn_edit.click()
    time.sleep(1)
    webtable.first_name.clear()
    time.sleep(1)
    webtable.first_name.send_keys("Timmy")
    webtable.btn_submit.click()
    time.sleep(2)

    webtable.btn_delete.click()
    assert not webtable.newstr.get_dom_attribute('class') == 'rt-tr -odd'



