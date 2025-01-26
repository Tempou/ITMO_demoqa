from pages.form_page import FormPage
from conftest import browser

def test_login_form_validate(browser):
    login_page = FormPage(browser)

    login_page.visit()
    assert login_page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert login_page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert login_page.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert login_page.user_email.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
    login_page.btn_submit.click_force()
    assert login_page.validated_form.get_dom_attribute('class') == 'was-validated'



