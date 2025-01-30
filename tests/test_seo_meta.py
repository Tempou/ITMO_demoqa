from pages.accordian import AccordianPage
from pages.alerts_page import AlertsPage
from pages.demoqa import Demoqa
from pages.browserwindows_page import BrowserWindowsPage

from conftest import browser
import pytest
import time

@pytest.mark.parametrize('pages', [Demoqa, AccordianPage, AlertsPage, BrowserWindowsPage])
def test_meta(browser, pages):
    page = pages(browser)
    page.visit()

    assert page.viewport.exists()
    assert page.viewport.get_dom_attribute('name') == 'viewport'
    assert page.viewport.get_dom_attribute('content') == 'width=device-width,initial-scale=1'





