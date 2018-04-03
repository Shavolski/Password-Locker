from user import User
from credentials import Credentials
import random


def greetings():
    print("                           __      __               ")
    print(" /\      /\               |  |    |  |              ")
    print("|  |    |  |    ________  |  |    |  |      _____   ")
    print("|  |____|  |   |   ___  | |  |    |  |     /     \  ")
    print("|   ____   |   |  |___| | |  |    |  |    |  ___  | ")
    print("|  |    |  |   |  ______| |  |__  |  |__  | |___| | ")
    print("|  |    |  |   | |______  |     | |     | |       | ")
    print(" \/      \/     \_______/ \_____/  \____/  \_____/  ")

greetings()

def password (password):
    '''
    Function to rewrite the Value error to make it easier to understand
    '''
    print("Create new password ")
    try:
        number = int(input())
        return number
    except ValueError:
        return "That was not a valid input"
def create_contact(fname, lname, password, email):
    '''
    Function to create a new contact
    '''
    new_user = User(fname, lname, password, email)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user():
    '''
    Function to delete a user
    '''
    contact.delete_user()

def find_user(password):
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_by_password(password)

def check_existing_user(password):
    '''
    Function that check if a user exists with that password and return a Boolean
    '''
    return User.user_exist(password)

def display_user():
    '''
    Function that returns all the saved user
    '''
    return user.display_user()

def main():
    print("...........Whatsup Huuuumaaan?.This is the place where I, the bot, make passwords for you. What is your name?...........")
    user_name = input()

    print(f"........Waddup {user_name}. my master (Developer) wants me to assist you in making a user account.......")
    print('\n')

    while True:
            print(
                "Yo human...Use these short codes to walk through around my master's app : cu - create a new user, dc - display user, fc -find a user, ex -exit the user list")

            short_code = input().lower()

            if short_code == 'cu':
                    print("...............New User.............")
                    print("-"*10)
                    print("-"*10)

                    print("...............Pop up your First name...............")
                    f_name = input()
                    print("-"*10)

                    print("...............Pop up your Last name...............")
                    l_name = input()
                    print("-"*10)

                    print("..................Let me do the magic in making your Password................")
                    random_number = random.randint(1000,9999)
                    print(random_number)
                    print("-"*10)

                    print(".................Email address..................")
                    e_address = input()
                    print("-"*10)
                    print("-"*10)

                    # create and save new contact.
                    save_user(create_user(f_name,l_name,password,e_address))
                    print('\n')
                    print(f"New User {f_name} {l_name} created")
                    print('\n')

            elif short_code == 'dc':

                    if display_users():
                            print("Here is a list of all your user")
                            print('\n')

                            for user in display_users():
                                    print(
                                        f"{user.first_name} {user.last_name} .....{user.password}")

                            print('\n')
                    else:
                            print('\n')
                            print(
                                "you don't have any")
                            print('\n')

            elif short_code == 'fc':

                    print("Enter the password you want to search for")

                    search_password = input()
                    if check_existing_user(search_password):
                            search_user = find_user(
                                search_password)
                            print(
                                f"{search_user.first_name} {search_user.last_name}")
                            print('-' * 20)

                            print(
                                f"Password.......{search_user.password}")
                            print(
                                f"Email address.......{search_user.email}")
                    else:
                            print("Again I don't get it")

            elif short_code == "ex":
                    print("Adios!.......")
                    break
            else:
                    print(
                        "I'm a bot I can't. PLEASE use the short codes")

if __name__ == '__main__':
    main()
