import unittest
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in reating test cases.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Steve","Wachira")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test of the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Steve")
        self.assertEqual(self.new_user.last_name,"Wachira")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user_list
        '''
        self.new_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user check if we can save multiple user objects to our user_lists
        '''
        self.new_user.save_user()
        test_user = User("Test","user",)
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user user_list
        '''
        self.new_user.save_user()
        test_user = User("Test","user")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)

    def test_find_user_by_name(self):
        '''
        test to check if we can find a user by name and display information
        '''
        self.new_user.save_user()
        test_user = User("Test","user")
        test_user.save_user()
        found_user = User.find_by_name("Steve")
        self.assertEqual(found_user.name)

    def test_contact_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_user.save_user()
        test_user = User("Test", "user")
        test_user.save_user()

        user_exists = User.user_exist("Steve")

        self.assertTrue(user_exists)

    def test_display_all_user(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(), User.user_list)
  #This is the test for the credentials
class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in reating test cases.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = Contact("Steve","Wachira","0714091244","steve@moringaschool.com")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Contact.contact_list = []

    def test_init(self):
        '''
        test_init test case to test of the object is initialized properly
        '''
        self.assertEqual(self.new_contact.phone_number,"0714091244")
        self.assertEqual(self.new_contact.email,"steve@moringaschool.com")

    def test_save_contacts(self):
        '''
        test_save_contacts test case to test if the contact object is saved into the contact list
        '''
        self.new_contact()
        self.assertEqual(len(Contact.contact_list),1)

    def test_save_multiple_contact(self):
        '''
        test_save_multiple_contact check if we can save multiple contact objects to our contact_lists
        '''
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0714091244","test@user.com")
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),2)

    def test_delete_contact(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact contact_list
        '''
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0714091244","test@user.com")
        test_contact.save_contact()
        self.new_contact.delete_contact()
        self.assertEqual(len(Contact.contact_list), 1)

    def test_find_contact_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0714091244","test@user.com")
        test_contact.save_contact()
        found_contact = Contact.find_by_number("0714091244")
        self.assertEqual(found_contact.email, test_contact.email)

    def test_contact_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0711223344",
                               "test@user.com")  # new contact
        test_contact.save_contact()

        contact_exists = Contact.contact_exist("0711223344")

        self.assertTrue(contact_exists)

    def test_display_all_contacts(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(Contact.display_contacts(), Contact.contact_list)

    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found contact
        '''

        self.new_contact.save_contact()
        Contact.copy_email("0712345678")

        self.assertEqual(self.new_contact.email, pyperclip.paste())

if __name__ == '__main__'
    unittest.main()
