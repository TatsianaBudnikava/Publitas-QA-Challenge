from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import BasePageLocators

class SlideshowPage(BasePage):

    def should_be_images_displaying(self):
        try:
            self.browser.find_element(*BasePageLocators.STEPPER_forward_btn).click()
            self.browser.find_element(*BasePageLocators.STEPPER_forward_btn).click()
            self.browser.find_element(*BasePageLocators.STEPPER_forward_btn).click()
            self.browser.find_element(*BasePageLocators.STEPPER_forward_btn).click()
            self.browser.find_element(*BasePageLocators.STEPPER_forward_btn).click()
            self.browser.find_element(*BasePageLocators.COUNTER)
            self.browser.find_element(*BasePageLocators.IMAGES)
            return True
        except NoSuchElementException:
            return False