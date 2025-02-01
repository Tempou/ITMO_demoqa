from pages.base_page import BasePage
from components.components import WebElement

class SliderPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/slider'
        super().__init__(driver, self.base_url)

        self.slider = WebElement(self.driver, '#sliderContainer > div.col-9 > span > input')
        self.slider_result = WebElement(self.driver, '#sliderValue')