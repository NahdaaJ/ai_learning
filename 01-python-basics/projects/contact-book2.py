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
            
def validate_input(prompt, option_list):
    user_input = ""
    
    while (user_input not in option_list):
        user_input = input().lower().strip()
        
        if user_input not in option_list:
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

def search_contacts(name):
    contacts = view_contacts()
    contact_found = False
    contact_info = []
    
    for row in contacts:
        for key, value in row.items():
            contact_found = value == name
            if contact_found:
                contact_info.append(row)
                break
            
    return contact_info   
    
def delete_contact(name, index):
    rows = []
    delete_contact = search_contacts(name)[index]
    
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row != delete_contact:
                rows.append(row)
    
    with open(file_path, "w") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        
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
            
        menu_input = validate_input("\nPlease enter a valid number (1-5).", ["1", "2", "3", "4", "5"])
        
        if (menu_input == "1"):
            search_input = input("Please enter the contact you want to search: ").lower().strip()
            
            search_result = search_contacts(search_input)
            
            if search_result == []:
                print("\nContact not found.")
            else:
                print(f"\n{len(search_result)} search result(s) found.\n")
                for row in search_result:
                    for key, value in row.items():
                         print(f"{key}: {value.title()}")
                    print("\n")
            input("Press enter to return to main menu.")
            
        elif (menu_input == "2"):
            print("\n")
            contacts = view_contacts()
            if contacts == []:
                print("No contacts found.")
            else:
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
                confirmation = validate_input("Please enter Y, N, or R. ", ["y", "n", "r"])
                
                if confirmation == "y": 
                    add_contact(name, number, city)
                    print("\n\nContact added.")
                    input("Press enter to return to main menu.")
            
        elif (menu_input == "4"):
            contact_name = input("Please enter the contact you want to delete: ").lower().strip()
            contact_index = 0
            
            search_result = search_contacts(contact_name)
            
            if search_result == []:
                print("\nContact not found.")
                input("Press enter to return to main menu.")
                continue
            
            print(f"\n{len(search_result)} search result(s) found.\n")
            for index,row in enumerate(search_result):
                if len(search_result) > 1:
                    print(index)
                    for key, value in row.items():
                            print(f"{key}: {value.title()}")
                    print("\n")
            print(f"Please enter the contact you wish to delete (0-{len(search_result)-1}):")
            validation_number = [str(i) for i in range(len(search_result))]
            prompt = f"Please enter a valid number (0-{len(search_result)-1})."
            contact_index = int(validate_input(prompt, validation_number))                

            print("-------------------------------")
            for key,value in search_result[contact_index].items():
                print(f"{key}: {value.title()}") 
                
            print("\nDelete this contact? (Y/N)")
            confirmation = validate_input("Please enter Y or N.", ["y", "n"])
            
            if confirmation == "y":
                delete_contact(contact_name, contact_index)
                print("\nContact deleted.")
                    
            input("Press enter to return to main menu.")  
            
        elif (menu_input == "5"):
            print("Goodbye!")
            exit()
        
initialisation()
main_menu()