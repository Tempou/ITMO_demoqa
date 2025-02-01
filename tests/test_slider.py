from selenium.webdriver import Keys
from pages.slider_page import SliderPage
from conftest import browser
import time

def test_slider(browser):
    slider_page = SliderPage(browser)

    slider_page.visit()
    assert  slider_page.slider.exists()
    assert  slider_page.slider_result.exists()

    assert slider_page.slider.get_dom_attribute('value') == '25'
    assert slider_page.slider_result.get_dom_attribute('value') == '25'

    while not slider_page.slider.get_dom_attribute('value') == '50':
        slider_page.slider.send_keys(Keys.ARROW_UP )
    time.sleep(2)

    assert slider_page.slider_result.get_dom_attribute('value') == '50'
