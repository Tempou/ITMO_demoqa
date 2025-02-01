from pages.progressbar_page import ProgressbarPage
from conftest import browser
import time

def test_pb(browser):
    bp_page = ProgressbarPage(browser)

    bp_page.visit()
    assert bp_page.progress_bar.exists()
    time.sleep(2)

    bp_page.btn_start.click()

    while True:
        if bp_page.progress_bar.get_dom_attribute('aria-valuenow') == '51':
            bp_page.btn_start.click()
            break

    time.sleep(2)