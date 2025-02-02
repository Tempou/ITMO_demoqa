from pages.accordian import AccordianPage
from pages.alerts_page import AlertsPage
from pages.demoqa import Demoqa
from pages.browserwindows_page import BrowserWindowsPage

from conftest import browser
import pytest
import time


def test_title(browser):
    demoqa_page=Demoqa(browser)
    demoqa_page.visit()

    assert browser.title == 'DEMOQA'


@pytest.mark.parametrize('pages', [Demoqa, AccordianPage, AlertsPage, BrowserWindowsPage])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)

    assert page.get_title() == 'DEMOQA'


