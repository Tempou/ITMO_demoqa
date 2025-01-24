from pages.demoqa import Demoqa
from conftest import browser

def test_title(browser):
    demoqa_page=Demoqa(browser)
    demoqa_page.visit()

    assert browser.title == 'DEMOQA'

