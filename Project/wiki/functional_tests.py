from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from django.test import LiveServerTestCase

#FUNCTIONAL_TESTS for login and user management

class NewVisitorTest(LiveServerTestCase):

	## start a new browser session to test inside of##
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3) 

	## quit the web browser session
	def tear_Down(self):
		self.browser.quit()



	
	
	
	def test_can_login(self):
	#Mike  has recently taken interest in gardening and has heard about a wiki to do with growing
		self.browser.get(self.live_server_url)

	#He notices that the title and header mention gardening wiki
		##Title assertion
		self.assertIn('Wiki' , self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Wiki', header_text)



		#An inputbox is waiting for his login details input
		## test to see if input box exists and contains text
		inputbox = self.browser.find_element_by_id('uname_field')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'username'
		)

	
        un_input = self.browser.find_element_by_id('uname_field')
        un_input.send_keys('GreenThumbGary')

        pw_input = self.browser.find_element_by_id('pword_field')
        pw_input.send_keys('Iam100Green')

        #He logs in

        inputbox.send_keys(Keys.ENTER)

    def test_register_new_user(self):
    	#Jerry opens the register page and enters his details in

    	self.assertIn('Wiki' , self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Register', header_text)

		un_input = self.browser.find_element_by_id('uname_field')
        un_input.send_keys('GreenThumbGary')

        pw_input = self.browser.find_element_by_id('pword_field')
        pw_input.send_keys('Iam100Green')
    
        fn_input = self.browser.find_element_by_id('id_firstname')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'firstname'
		)

        fn_input = self.browser.find_element_by_id('id_first_name')
        fn_input.send_keys('Gary')

       	ln_input = self.browser.find_element_by_id('id_new_student')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'lastname'
		)

        ln_input = self.browser.find_element_by_id('id_last_name')
        ln_input.send_keys('Johnson')

        

        ln_input = self.browser.find_element_by_id('email_text')
        ln_input.send_keys('gj@gmail.com')

        bday_input = self.browser.find_element_by_id('id_new_student')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'YYYY/MM/DD'
		)

        bday_input = self.browser.find_element_by_id('bday_text')
        bday_input.send_keys('1988/05/13')

		inputbox.send_keys(Keys.ENTER)


		bday_input = self.browser.find_element_by_id('bday_text')
		self.assertIn()

		#He notices that he has been redirected and logs in with his new user details

		un_input = self.browser.find_element_by_id('uname_field')
        un_input.send_keys('GreenThumbGary')

        pw_input = self.browser.find_element_by_id('pword_field')
        pw_input.send_keys('Iam100Green')

        logged_in = self.browser.find_element_by_id('h2')

        #He sees that he is logged in
      	self.assertIn(logged_in, 'GreenThumbGary')

        self.fail('FInish the test')

      