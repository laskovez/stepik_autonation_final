from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = self.url
        assert "login" in login_link, "Login link not content the 'login' word"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        login_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS)
        password_conf = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS_CONF)
        login_field.send_keys(email)
        password_field.send_keys(password)
        password_conf.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        registration_button.click()

