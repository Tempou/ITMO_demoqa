from components.components import WebElement
from pages.base_page import BasePage


class AccordianPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.content=WebElement(self.driver, '#section1Content > p')
        self.heading=WebElement(self.driver, '#section1Heading')
        self.section2content=WebElement(self.driver, '#section2Content')
        self.section3content=WebElement(self.driver, '#section3Content')
