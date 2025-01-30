from components.components import WebElement
from pages.base_page import BasePage


class AlertsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        self.btn_alert = WebElement(self.driver, '#alertButton')
        self.btn_confirm = WebElement(self.driver, '#confirmButton')
        self.btn_prompt = WebElement(self.driver, '#promtButton')
        self.confirm_result = WebElement(self.driver, '#confirmResult')
        self.prompt_result = WebElement(self.driver, '#promptResult')