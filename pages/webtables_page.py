from pages.base_page import BasePage
from components.components import WebElement

class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'

        super().__init__(driver, self.base_url)

        self.btn_delete_row = WebElement(driver, '//span[@title="Delete"]', 'xpath')
        self.no_data = WebElement(driver, 'div.rt-noData')
