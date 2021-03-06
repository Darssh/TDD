from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
	
	def test_cannot_add_empty_list_items(self):
		self.browser.get(self.server_url)
		self.get_item_input_box().send_keys('\n')

		self.get_item_input_box().send_keys('Buy milk\n')
		self.check_for_row_in_list_table('1: Buy milk')

		self.get_item_input_box().send_keys('\n')

		self.check_for_row_in_list_table('1: Buy milk')

		self.get_item_input_box().send_keys('Make tea\n')
		self.check_for_row_in_list_table('1: Buy milk')
		self.check_for_row_in_list_table('2: Make tea')


	def test_cannot_add_duplicate_items(self):
	    # Edith goes to the home page and starts a new list
	    self.browser.get(self.server_url)
	    self.get_item_input_box().send_keys('Buy wellies\n')
	    self.check_for_row_in_list_table('1: Buy wellies')

	    # She accidentally tries to enter a duplicate item
	    self.get_item_input_box().send_keys('Buy wellies\n')

	    # She sees a helpful error message
	    self.check_for_row_in_list_table('1: Buy wellies')
	    error = self.browser.find_element_by_css_selector('.has-error')
	    self.assertEqual(error.text, "You've already got this in your list")


	def test_error_messages_are_cleared_on_input(self):
	    # Edith starts a new list in a way that causes a validation error:
	    self.browser.get(self.server_url)
	    self.get_item_input_box().send_keys('\n')
	    error = self.browser.find_element_by_css_selector('.has-error')
	    self.assertTrue(error.is_displayed())  

	    # She starts typing in the input box to clear the error
	    self.get_item_input_box().send_keys('a')

	    # She is pleased to see that the error message disappears
	    error = self.browser.find_element_by_css_selector('.has-error')
	    self.assertFalse(error.is_displayed()) 