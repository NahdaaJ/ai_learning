import csv
import os
file_path = '../test-files/contact-book.csv'
field1 = "Name"
field2 = "Number"
field3 = "City"
fieldnames = [field1, field2, field3]


def initialisation():
    if not os.path.exists(file_path):
        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
def validate_input(prompt, *options):
    user_input = ""
    
    while (user_input not in options):
        user_input = input().lower().strip()
        
        if user_input not in options:
            print(prompt)
            
    return user_input   
    
def add_contact(name, number, city):
    data = {field1: name, field2: number, field3: city }
    with open(file_path, 'a', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(data)

def view_contacts():
    contacts = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            contacts.append(row)
            
    return contacts
        
def main_menu():
    menu_input = ""
    
    while (menu_input != "1" or menu_input != "2" or menu_input != "3" or menu_input != "4"):
        print('''
========== MENU ==========
1 - Search a contact,
2 - View all contacts,
3 - Add a contact,
4 - Delete a contact, 
5 - Exit
        ''')
            
        menu_input = validate_input("\nPlease enter a valid number (1-5).", "1", "2", "3", "4", "5")
        
        if (menu_input == "1"):
            print("Searching..")
            
        elif (menu_input == "2"):
            print("\n")
            contacts = view_contacts()
            for row in contacts:
                for key,value in row.items():
                    print(f"{key}: {value.title()}")
                    
                print("\n")
            input("Press enter to return to main menu.")
            
        elif (menu_input == "3"):
            confirmation = "n"
            while confirmation == "n":
                name = input("Please enter the contact name: ").lower().strip()
                number = input("Please enter the contact's number: ").strip()
                city = input("Please enter the contact's city: ").lower().strip()
                
                print(f"\nName: {name.title()}\tNumber: {number}\tCity: {city.title()}")
                print("Is this correct? (Y/N)\nOr return to Main Menu (R) ")
                confirmation = validate_input("Please enter Y, N, or R. ", "y", "n", "r")
                
                if confirmation == "y": 
                    add_contact(name, number, city)
                    print("\n\nContact added.")
                    input("Press enter to return to main menu.")
            
        elif (menu_input == "4"):
            print("Deleting..")    
            
        elif (menu_input == "5"):
            print("Goodbye!")
            exit()
        
initialisation()
main_menu()