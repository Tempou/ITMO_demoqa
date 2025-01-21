from pages.elements_page import ElementsPage


def test_check_footer_text(browser):
    footer_text = ElementsPage(browser)

    footer_text.visit()
    assert footer_text.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    assert footer_text.center_element.get_text() == 'Please select an item from left to start practice.'