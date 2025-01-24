from pages.elements_page import ElementsPage
from pages.demoqa import Demoqa

def test_navigation(browser):
    demoqa_page=Demoqa(browser)
    element_page=ElementsPage(browser)

    demoqa_page.visit()
    demoqa_page.btn_elements.click()

    demoqa_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()

    assert element_page.equal_url()
