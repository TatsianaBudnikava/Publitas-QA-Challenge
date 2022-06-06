from selenium.webdriver.common.by import By


class BasePageLocators():
    STEPPER_forward_btn = (By.CSS_SELECTOR, "[type='button']:nth-of-type(2)")
    STEPPER_back_btn = (By.CSS_SELECTOR, "[type='button']:nth-of-type(1)")
    COUNTER = (By.XPATH, '(//div[normalize-space()="5 / 5"])[2]')
    IMAGIES = (By.CSS_SELECTOR, '[aria-hidden="false"]')