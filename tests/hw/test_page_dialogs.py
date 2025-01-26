from pages.dialogs_page import ModalDialogs
from conftest import browser
from pages.demoqa import Demoqa

def test_modal_dialogs(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()

    assert modal_dialogs.btns_under_menu.check_count_elements(count = 5)


def test_navigation_dialogs(browser):
    navigation_modal = ModalDialogs(browser)
    demoqa_page = Demoqa(browser)
    navigation_modal.visit()

    navigation_modal.refresh()
    navigation_modal.main_page.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert demoqa_page.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)








