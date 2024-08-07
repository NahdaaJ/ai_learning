# Creation
def greet_friend1(name):
	greeting = f"Hello {name}! How are you?"
	return greeting
	
# Creation with a default value
def greet_friend2(name="friend"):
	greeting = f"Hello {name}!"
	return greeting

## Calling function
my_greeting = greet_friend1("Nahdaa")
print(my_greeting)

print(greet_friend2())
print(greet_friend2("Nahdaa"))

print("\n\n")


# -------------------------------------------------------------------------
# Unpacking Tuples
def highest_price(price_list):
    max_price = 0
    max_item = ""
    
    for item, price in price_list:
        if price > max_price:
            max_price = price
            max_item = item
            
    return (max_item, max_price)

price_list = [("Banana", 2.89), ("Strawberry", 5.80), ("Apple", 3.10)]
item, price = highest_price(price_list)

print(item)
print(price)
print("\n\n")


# -------------------------------------------------------------------------
# *args and **kwargs

def add_nums(*args):
    return sum(args)

print(add_nums(1,2))
print(add_nums(14565,3,234,264,65))

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Nahdaa", age=24, job="engineer")

def my_func(*args, **kwargs):
    if len(args) != len(kwargs):
        print("Args and Kwargs differ in length.")
        return
    
    kwargs_values = list(kwargs.values())
    for i in range(len(args)):
        print(f"I want {args[i]} {kwargs_values[i]}.")
        
my_func(31,42,45, food="kebab", pet="daschund", sweets="maoams")
print("\n\n")

# -------------------------------------------------------------------------
# Map  and Filter function
def square(num):
    return num*num

my_nums = [1,2,3,4,5]

for item in map(square, my_nums):
    print (item)
    
# or

map_list = list(map(square, my_nums))
print(map_list)
print(type(map_list))


def check_for_letter(letter):
    return "n" == letter or "t" == letter

filter_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris non interdum sem. Etiam sit amet elementum nisi. Vivamus augue orci, iaculis in lacus a, vehicula fermentum eros"
filtered_letters = list(filter(check_for_letter, filter_string))
print(filtered_letters)

print("\n\n")

# -------------------------------------------------------------------------
# Lambda Functions

# instead of 
def multiple(num1, num2):
    result = num1 * num2
    return result

# you can do
lambda num1, num2: num1 * num2

# can be used in conjuction with map and filter
lambda_nums = [1,6,2,6]
lambda_nums2 = [3,9,4,6]

lambda_list = list(map(lambda num1, num2: num1 * num2, lambda_nums, lambda_nums2))
print(lambda_list)

print("\n\n")

# -------------------------------------------------------------------------
# Nested Statements and Scope

x = 50 # Global x

def my_func():
    global x #everything that happens to x inside here affects the one globally.
    print(f"X is {x}")
    
    x = 200

my_func()
print(f"X is now {x}")