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

if __name__ == '__main__'
    unittest.main()
