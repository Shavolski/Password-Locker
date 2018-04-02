class Credentials:
    """
    Class that generates new instances of credentials
    """
    credential_list = []

    def __init__(self,password,email):
        self.password = password
        self.email = email

    credential_list = []

    def save_credential(self):
        '''
        save_credential method saves  objects into credential_list
        '''
        Credential.credential_list.append(self)
    def delete_credential(self):
        '''
        delete_credential method deletes a saved credential from the credential_list
        '''
        Credential.credential_list.remove(self)
    @classmethod
    def find_by_password(cls, password):
        '''
        Method that takes in a password and returns a credential that matches that password.

        Args:
            password: password to search before
        Returns:
           Credential of person that matches the password
        '''
        for credential in cls.credential_list:
            if.credential.password == password:
                return credential
    @classmethod
    def credential_exist(cls, password):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            password: password to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.password == password:
                    return True

        return False

    @classmethod
    def display_credential(cls):
        '''
        method that returns the credential list

        credential_found = Credential.find_by_password(password)
        '''
        return cls.credential_list
    @classmethod
    def copy_email(cls, password):
        pyperclip.copy(credential_found.email)
