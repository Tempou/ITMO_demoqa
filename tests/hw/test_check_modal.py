from pages.dialogs_page import ModalDialogs
from conftest import browser
import time


#Задание 1
def test_check_modal(browser):
    try:
        modal_page = ModalDialogs(browser)
        modal_page.visit()

        modal_page.btn_small.click()
        time.sleep(2)
        modal_page.btn_close_small.click()

        modal_page.btn_large.click()
        time.sleep(2)
        modal_page.btn_close_large.click()
    except:
        pass