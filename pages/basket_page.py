from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
	def check_text_for_empty_cart_guest(self):
		self.is_element_present(*BasketPageLocators.CART_TEXT)



