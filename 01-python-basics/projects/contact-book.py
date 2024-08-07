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
            search_contacts()
        
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
            
def search_contacts():
    print("Searching....")

def view_contacts():
    if (len(contacts) == 0):
        print("Contact book empty.")
    else:
        for key, value in contacts.items():
            print(f"{key.title()}: {value}")
            
    input("\nPress enter to return to main menu.")        
    main_menu()
    
def add_contacts():
    print("Adding....")
    
def delete_contacts():
    print("Deleting....")


contacts = {
    "nahdaa": 12341234432,
    "john": 33453453,
    "sara": 29342394
    }
main_menu()