from components.components import WebElement
from pages.base_page import BasePage

class FormPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement('#firstName')
        self.last_name = WebElement('#lastName')
        self.user_email = WebElement('#userEmail')
        self.gender_radio_1 = WebElement('#gender-radio-1')
        self.user_number = WebElement('#userNumber')
        self.btn_submit = WebElement('#submit')
        self.modal_dialog = WebElement('body > div.fade.modal.show > div')
        self.btn_close_modal = WebElement('#closeLargeModal')