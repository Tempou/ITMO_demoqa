from pages.webtables_page import WebTables
from conftest import browser
import time


#Задача 1
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


#Задача 2*
def test_webtables2(browser):
    webtable = WebTables(browser)

    webtable.visit()
    webtable.rows_scroll.click()
    webtable.rows_scroll_5.click()
    time.sleep(2)
    assert webtable.btn_next.get_dom_attribute('disabled') == 'true'
    assert webtable.btn_prev.get_dom_attribute('disabled') == 'true'

################################Для себя на будущее
    for i in range(5):
        webtable.btn_add.click()
        webtable.first_name.send_keys("123")
        webtable.last_name.send_keys("123")
        webtable.email.send_keys("ttt1tt@ttt.com")
        webtable.age.send_keys("22")
        webtable.salary.send_keys("199831")
        webtable.department.send_keys("Department")
        webtable.btn_submit.click()
    time.sleep(1)

    webtable.btn_add.click()
    webtable.first_name.send_keys("Ti1m")
    webtable.last_name.send_keys("Cap1ello")
    webtable.email.send_keys("ttt4tt@ttt.com")
    webtable.age.send_keys("22")
    webtable.salary.send_keys("199831")
    webtable.department.send_keys("Department")
    webtable.btn_submit.click()
    time.sleep(1)

    webtable.btn_add.click()
    webtable.first_name.send_keys("1313Tim")
    webtable.last_name.send_keys("C1313apello")
    webtable.email.send_keys("tt5ttt@ttt.com")
    webtable.age.send_keys("22")
    webtable.salary.send_keys("199831")
    webtable.department.send_keys("Department")
    webtable.btn_submit.click()
    time.sleep(1)
    assert not webtable.btn_next.get_dom_attribute('disabled') == 'true'
    assert webtable.btn_prev.get_dom_attribute('disabled') == 'true'

    webtable.btn_next.click()
    assert not webtable.btn_prev.get_dom_attribute('disabled') == 'true'
    assert webtable.btn_next.get_dom_attribute('disabled') == 'true'
    time.sleep(2)

    webtable.btn_prev.click()
    assert not webtable.btn_next.get_dom_attribute('disabled') == 'true'
    assert webtable.btn_prev.get_dom_attribute('disabled') == 'true'
    time.sleep(2)










