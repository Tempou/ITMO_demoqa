from components.components import WebElement
from pages.base_page import BasePage


class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.footer=WebElement(driver, '#app > footer > span')
        self.center_element = WebElement(self.driver, '#app > div > div > div > div.col-12.mt-4.col-md-6')
        self.icon = WebElement(self.driver, 'header > a > img')
        self.btn_sidebar_first = WebElement(driver, '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(1) > span')
        self.btn_sidebar_first_textbox = WebElement(driver, '#item-0')
        self.btn_sidebar_first_checkbox = WebElement(driver, '#item-1')
        self.btns_first_menu = WebElement(driver, '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(1) > div > ul > li')
