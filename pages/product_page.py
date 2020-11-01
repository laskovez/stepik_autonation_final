from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def add_item_t0_the_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_button.click()

    # def get_item_name(self):
    #     item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
    #     #print(item_name.text)

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "Login link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_the_success_message(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_SUCCESS_MESSAGE).text == \
               self.browser.find_element(*ProductPageLocators.ITEM_NAME).text, "Success Message not equal with" \
                                                                               " the expected"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEM_SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ITEM_SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"


