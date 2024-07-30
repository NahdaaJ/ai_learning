from random import shuffle
from random import randint

def if_elif_else(my_age):
    if my_age < 18:
        print("You are a baby!")
    elif my_age > 18:
        print("You are a granny!")
    else:
        print("You're an adult now!")
        
def for_loops():
    my_family = ["Trung", "Ammu", "Zayn", "Nael"]
	
    for member in my_family:
        print(f"I love {member}!")
        
    my_nums = [(1,2,3), (4,5,6), (7,8,9)]
    
    for a,b,c in my_nums:
        print(b)
        
def while_loops(): 
    x = 0
    
    while x < 5:
        print(f"Current number: {x}")
        x += 1
        
    else: 
        print("X is now greater than or equal to 5.")
        
def break_continue():
    my_name = "Nahdaa"
    
    for letter in my_name:
        if letter == "a":
            continue
            # break
        print(letter)
        
def enumerate_demo():
    my_name = "Nahdaa"
    
    # for letter in enumerate(my_name):
    #     print(letter)
        
    for index,letter in enumerate(my_name):
        print(f"At index {index} is letter {letter}")

def zip_demo():
    list1 = [4,5,6]
    list2 = ["B", "C", "D"]
    list3 = [True, False, True]
    
    for item in zip(list1, list2, list3):
        print(item)
        
    # my_combined_list = list(zip(list1, list2, list3))
    
    # for item in my_combined_list:
    #     print(item)
    
def in_demo():
    # print('x' in [1,2,3])
    # print('x' in ["x","y","z"])
    # print('x' in "Nahdaa")
    # print('N' in "Nahdaa")
    
    my_dict = {"name": "Nahdaa", "age": 24}
    print("name" in my_dict)
    print(24 in my_dict.values())
    print(24 in my_dict.keys())

def min_max():
    my_list = [1,4,76,4535,2,345,6456,1,4,6,0,456,1]
    print(min(my_list))
    print(max(my_list))
    
def random_demo():
    x = randint(1,10)
    my_list = [1,2,3,4,5]
    shuffle(my_list)
    
    print(x)
    print(my_list)
     
# if_elif_else(24)
# for_loops()
# while_loops()
# break_continue()
# enumerate_demo()
# zip_demo()
# in_demo()
# min_max()
# random_demo()