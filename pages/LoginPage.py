from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.XPATH, '//*[@id="field_email"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="field_password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    QR_LINK = (By.XPATH, '//*["@data-l="t,get_qr"]')
    REGISTER_LINK = (By.XPATH, '//*[@data-l="t,register"]')
    VK_LINK = (By.XPATH, '//*[@data-l="t,vkc"]')
    MAIL_LINK = (By.XPATH, '//*[@data-l="t,mailru"]')
    GOOGLE_LINK = (By.XPATH, '//*[@data-l="t,google"]')
    YANDEX_LINK = (By.XPATH, '//*[data-l="t,yandex"]')
    APPLE_LINK = (By.XPATH, '//*[@data-l="t,apple"]')
    ENTER_TAB_LINK = (By.XPATH, '//*[@data-l="t,login_tab"]')
    QR_TAB_LINK = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    ERROR_FIELD = (By.XPATH, '//*[@class="input-e login_error"]')

class LoginPageHelper(BasePage):
    def __check_page(self):
        self.findElement(LoginPageLocators.LOGIN_FIELD)
        self.findElement(LoginPageLocators.PASSWORD_FIELD)
        self.findElement(LoginPageLocators.LOGIN_BUTTON)
        self.findElement(LoginPageLocators.QR_LINK)
        self.findElement(LoginPageLocators.REGISTER_LINK)
        self.findElement(LoginPageLocators.VK_LINK)
        self.findElement(LoginPageLocators.MAIL_LINK)
        self.findElement(LoginPageLocators.GOOGLE_LINK)
        self.findElement(LoginPageLocators.YANDEX_LINK)
        self.findElements(LoginPageLocators.APPLE_LINK)
        self.findElement(LoginPageLocators.ENTER_TAB_LINK)
        self.findElement(LoginPageLocators.QR_TAB_LINK)

    def click_login_button(self):
        login_button = self.findElement(LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def get_error_text(self):
        error_text = self.findElement(LoginPageLocators.ERROR_FIELD)
        return error_text.text