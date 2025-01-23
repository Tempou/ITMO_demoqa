from pages.elements_page import ElementsPage

def test_page_elements(browser):
    element_page = ElementsPage(browser)
    element_page.visit()

    assert element_page.icon.exists()
    assert element_page.btn_sidebar_first.exists()
    assert element_page.btn_sidebar_first_textbox.exists()







