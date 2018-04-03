class User:
    """
    Class that generates new instances of contacts
    """

    user_list = []

    def __init__(self,first_name,last_name,):
        self.first_name = first_name
        self.last_name = last_name

    contact_list = []

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)
    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_name(cls, name):
        '''
        Method that takes in a name and returns a contact that matches that name.

        Args:
            name: First or Last name to search before
        Returns:
                User of person that matches the name
        '''
        for user in cls.user_list:
            if user.name == name:
                return contact
    @classmethod
    def user_exist(cls, name):
        '''
        Method that checks if a user exists from the user list.
        Args:
            name: Name to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.name == name:
                    return True

        return False
