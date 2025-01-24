from pages.demoqa import Demoqa
from conftest import browser
import time

def test_size(browser):
    demoqa_page=Demoqa(browser)
    demoqa_page.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(3000, 3000)