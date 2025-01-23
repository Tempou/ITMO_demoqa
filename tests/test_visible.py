from pages.elements_page import ElementsPage
import time

def test_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.btn_sidebar_first_textbox.visible()


def test_not_visible_btn_sidebar(browser):
    element_page = ElementsPage(browser)

    element_page.visit()
    assert element_page.btn_sidebar_first_checkbox.visible()
    element_page.btn_sidebar_first.click()
    time.sleep(2)
    assert not element_page.btn_sidebar_first_checkbox.visible()



