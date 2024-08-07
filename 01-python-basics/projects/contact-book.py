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
    name = input ("\nPlease enter the name of the contact: ").title()
    number = input("Please enter the persons phone number: ")
    
    print(f"\n{name}: {number}")    
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
    print("Deleting....")


contacts = {}
main_menu()