from phonebook import Phonebook
def main():
    username = input("Enter username > ")
    print(f"Hello {username} how are you doing today?")
    while True:
        print("Use the following short codes to navigate: cc-create contact fc-find contact dc- display contacts dlc-delete contact ex-exit")
        short_code = input(">").lower()
        if short_code == 'cc':
            f_name = input("First name > ")
            l_name = input("Last name  > ")
            p_number = input("Phone number > ")
            mail = input("Email > ")

            new_contact = Phonebook(f_name, l_name, p_number, mail)
            new_contact.saveContact()
            print(f"New contact {new_contact.first_name} {new_contact.last_name} successfully created.")

        elif short_code == 'dc':
            index = 1
            for contact in Phonebook.displayContacts():
                print(f"{index}. Phone number: {contact[0]} \n First name: {contact[1].first_name} \n Last name: {contact[1].last_name} \n Email: {contact[1].email}")
                index += 1

        elif short_code == 'fc':
            number = input("Enter the number that you want to search > ")
            search_number = Phonebook.findContact(number)
            if search_number:
                print(f"First name: {search_number.first_name} \n Last name: {search_number.last_name} \n Email: {search_number.email}")
            else:
                print("Ooops that contact doesn't exist!")

        elif short_code == 'dlc':
            del_number = input("Enter the number you want to delete > ")
            delete_contact = Phonebook.deleteContact(del_number)

        else:
            if short_code == 'ex':
                print("Bye, see you next time!")
                break

if __name__ == '__main__':
    main()