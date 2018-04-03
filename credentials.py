import random

class Credentials:
    """
    Class that generates new instances of credentials
    """
    credentials_list = []

    def __init__(self,password,email):
        self.password = password
        self.email = email

    credentials_list = []

    def save_credentials(self):
        '''
        save_credentials method saves  objects into credentials_list
        '''
        Credentials.credentials_list.append(self)
    def delete_credentials(self):
        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''
        Credentials.credentials_list.remove(self)
    @classmethod
    def find_by_password(cls, password):
        '''
        Method that takes in a password and returns a credentials that matches that password.

        Args:
            password: password to search before
        Returns:
           Credentials of person that matches the password
        '''
        for credentials in cls.credentials_list:
            if credentials.password == password:
                return credentials
    @classmethod
    def credentials_exist(cls, password):
        '''
        Method that checks if a credentials exists from the credentials_list.
        Args:
            password: password to search if it exists
        Returns :
            Boolean: True or false depending if the credentials_exists
        '''
        for credentials in cls.credentials_list:
            if credentials.password == password:
                    return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials_list

        credentials_found = Credentials.find_by_password(password)
        '''
        return cls.credentials_list
    @classmethod
    def copy_email(cls, password):
        pyperclip.copy(credentials_found.email)
