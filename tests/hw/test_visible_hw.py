from pages.accordian import AccordianPage
import time

def test_visible_accordion(browser):
    accordian_page = AccordianPage(browser)

    accordian_page.visit()
    accordian_page.heading.click()
    time.sleep(2)
    assert not accordian_page.content.visible()


def test_visible_accordion_default(browser):
    accordian_page = AccordianPage(browser)

    accordian_page.visit()
    assert not accordian_page.section2content.visible()
    assert not accordian_page.section3content.visible()


