import pytest
from pages.demoqa import Demoqa
from pages.radiobtn_page import RadioBtn
from conftest import browser
import time


@pytest.mark.skip
def test_demoqa(browser):
    demoqa = Demoqa(browser)

    demoqa.visit()
    assert demoqa.caterogies.check_count_elements()

    for element in demoqa.caterogies.find_elements():
        assert element.text != ''


@pytest.mark.skipif(True, reason='пропуск')
def test_radiobtn(browser):
    radiobtn_page = RadioBtn(browser)

    radiobtn_page.visit()
    radiobtn_page.yes.click_force()
    assert radiobtn_page.result_text.get_text() == 'You have selected Yes'
    time.sleep(1)

    radiobtn_page.impressive.click_force()
    assert radiobtn_page.result_text.get_text() == 'You have selected Impressive'
    time.sleep(1)

    assert 'disabled' in radiobtn_page.no.get_dom_attribute('class')
    time.sleep(1)







