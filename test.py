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
class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in reating test cases.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credential("0714091244","steve@moringaschool.com")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_init(self):
        '''
        test_init test case to test of the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.password,"0714091244")
        self.assertEqual(self.new_credentials.email,"steve@moringaschool.com")

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the contact object is saved into the credentials_list
        '''
        self.new_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials check if we can save multiple credentials objects to our credentials_lists
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("0714091244","test@user.com")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove a credentials from our credentials credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("0714091244","test@user.com")
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_find_credentials_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''
        self.new_credentials.save_credentials()
        test_credentials.save_credentials()
        found_credentials = Credentials.find_by_password("1244")
        self.assertEqual(found_credentials.email, test_credentials.email)

    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("7112","test@user.com")
        test_credentials()

        credentials_exists = Credentials.credentials_exist("1244")

        self.assertTrue(credentials_exists)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(), credentials.credentials_list)

    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found credentials
        '''

        self.new_credentials.save_credentials()
        Credentials.copy_email("5678")

        self.assertEqual(self.new_credentials.email, pyperclip.paste())

if __name__ == '__main__'
    unittest.main()
