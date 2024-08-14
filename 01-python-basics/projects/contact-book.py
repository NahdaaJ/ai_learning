'''
Title: Contact Book Project
Date Finished: 14/08/2024

Aim: The aim of this project was to practice python basics such as loops, statements and functions.

Notes: As this is a quick project, I didn't want to spend too much time on this, however I would
like to improve some things if this were a bigger project:
- Promote DRY: I repeat confirmations and answer validation, I would like to put these in a func.
- SOC: I would like to deal with I/O in one function, while the rest deals with logic.
'''

def main_menu():
    print('''
          Please Choose an Option
          
          1 - Search contacts
          2 - View all contacts
          3 - Add a contact
          4 - Delete a contact
          5 - Exit''')
    
    menu_input = ""
    
    while (menu_input != "1" or menu_input != "2" or menu_input != "3" or menu_input != "4" or menu_input != "5"):
        menu_input = input()
        
        if (menu_input == "1"):
            contact_search = input("Please enter the name of the contact: ").lower().strip()
            search_contacts(contact_search)
        
        elif (menu_input == "2"):
            view_contacts()
            
        elif (menu_input == "3"):
            add_contacts()

        elif (menu_input == "4"):
            delete_contacts()
            
        elif (menu_input == "5"):
            print("Goodbye!")
            exit()
        else:
            print("Please enter a valid number.")
            
def search_contacts(key):
    if key in contacts:
        print(f"Name: {key.title()}\t Number: {contacts[key]}")
    else:
        print("Contact not found.")
    input("\nPress enter to return to main menu.")        
    main_menu()

def view_contacts():
    if (len(contacts) == 0):
        print("Contact book empty.")
    else:
        for key, value in contacts.items():
            print(f"{key.title()}: {value}")
            
    input("\nPress enter to return to main menu.")        
    main_menu()
    
def add_contacts():
    name = input ("\nPlease enter the name of the contact: ").lower().strip()
    number = input("Please enter the persons phone number: ")
    
    print(f"\n{name.title()}: {number}")    
    confirmation = ""
    while (confirmation != "y" or confirmation != "n"):
        confirmation = input("\nAre these details correct? (Y / N) ").lower()
        
        if (confirmation =="y"):
            contacts[name] = number
            break
        elif (confirmation == "n"):
            add_contacts()
        else:
            print("Please enter Y or N.\n")
            
    add_another = ""
    while (add_another != "y" or add_another != "n"):
        add_another = input("Would you like to add another contact? (Y / N) ").lower()
        
        if (add_another =="y"):
            add_contacts()
        elif (add_another =="n"):
            input("\nPress enter to return to main menu.")        
            main_menu()
        else: 
            print("Please enter Y or N.\n")   
    
def delete_contacts():
    key = input("Please enter the name of the contact you want to delete: ").lower().strip()
    if key in contacts:
        print(f"Name: {key.title()}\t Number: {contacts[key]}\nIs this the contact you would like to delete? (Y/N) ")
        confirmation = ""
        
        while confirmation != "y" and confirmation != "n":
            confirmation = input().lower()
            
            if confirmation == "y":
                del contacts[key]
                print("Contact deleted.")
            elif confirmation == "n":
                delete_contacts()
            else:
                print("\nPlease enter Y or N.")
            
    else:
        print("Contact not found.")
        
    input("\nPress enter to return to main menu.")        
    main_menu()


contacts = {}
main_menu()