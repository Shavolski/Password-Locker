from contact import Contact

def create_contact(fname, lname, phone, email):
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
    Function that check if a contact exists with that password and return a Boolean
    '''
    return User.user_exist(password)

def display_user():
    '''
    Function that returns all the saved user
    '''
    return user.display_user()

def main():
    print("Whatsup Huuuumaaan?.This is the place I the bot maakes passwprds for you. What is your name?")
    user_name = input()

    print(f"Waddup {user_name}. what would you like to do?")
    print('\n')

    while True:
            print(
                "Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

            short_code = input().lower()

            if short_code == 'cc':
                    print("New Contact")
                    print("-"*10)

                    print("First name ....")
                    f_name = input()

                    print("Last name ...")
                    l_name = input()

                    print("Phone number ...")
                    p_number = input()

                    print("Email address ...")
                    e_address = input()

                    # create and save new contact.
                    save_contacts(create_contact(
                        f_name, l_name, p_number, e_address))
                    print('\n')
                    print(f"New Contact {f_name} {l_name} created")
                    print('\n')

            elif short_code == 'dc':

                    if display_contacts():
                            print("Here is a list of all your contacts")
                            print('\n')

                            for contact in display_contacts():
                                    print(
                                        f"{contact.first_name} {contact.last_name} .....{contact.number}")

                            print('\n')
                    else:
                            print('\n')
                            print(
                                "You dont seem to have any contacts saved yet")
                            print('\n')

            elif short_code == 'fc':

                    print("Enter the number you want to search for")

                    search_number = input()
                    if check_existing_contacts(search_number):
                            search_contact = find_contact(
                                search_number)
                            print(
                                f"{search_contact.first_name} {search_contact.last_name}")
                            print('-' * 20)

                            print(
                                f"Phone number.......{search_contact.number}")
                            print(
                                f"Email address.......{search_contact.email}")
                    else:
                            print("That contact does not exist")

            elif short_code == "ex":
                    print("Bye .......")
                    break
            else:
                    print(
                        "I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()
