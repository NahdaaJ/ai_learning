# Methods and Functions

Functions allow us to create blocks of code than can be repeatedly executed, keeping code DRY. **Include validation within the function**, whether its for parameters being passed in or for the logic inside the functions.

Use `help(method)` to get an explanation of the method.

## Function Creation

Use the return method in a function, do not use print. All the outputting to the console should be done in one place.

| Function Property | Syntax | Description |
| --- | --- | --- |
| Creation, no parameters | `def say_hello():` | Used to create a function that takes no parameters. |
| Creation, parameters | `def say_hello(name):` | Used to create a function that must take one (or more) parameters. |
| Creation, default parameters | `def say_hello(name=”friend”):` | Used to create functions that can take a parameter. |

## `*args` and `**kwargs`

Used in functions where you have multiple parameters, but you do not want to specify every single parameter in the function definition.

`*args` → Arguments, returns a **tuple**.

`**kwargs` → Key Word Arguments, returns a **dictionary.**

```python
# Using *args ----------------------------------------------------------------
def add_nums(*args):
    return sum(args)

print(add_nums(1,2))
print(add_nums(14565,3,234,264,65))

# Using **kwargs -------------------------------------------------------------
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Nahdaa", age=24, job="engineer")
```

## Lambda Expressions Map and Filter

`map(function, iterable)` → use the map function to apply the function to every item in the iterable. Can be casted to a list.

```python
def square(num):
    return num*num

my_nums = [1,2,3,4,5]

map_list = list(map(square, my_nums))
print(map_list)
# returns [1,4,9,16,25]
```

`filter(function, iterable)` → Checks which values return “true” in the iterable when using a function. Returns all that have value true.

```python
def check_for_letter(letter):
    return "n" == letter or "t" == letter
    
filter_string = "nahdaa ate icecream in the park with her nephew."
filtered_letters = list(filter(check_for_letter, filter_string))
print(filtered_letters)
# returns ['n', 't', 't', 't', 'n']
```

`lambda parameters: return logic` → anonymous functions, i.e. one time, temporary, unnamed functions. Can be used in conjuction with `map()` and `filter()`.

```python
# instead of 
def multiple(num1, num2):
    result = num1 * num2
    return result

# you can do
lambda num1, num2: num1 * num2

# using in cojunction with map() and filter()
lambda_nums = [1,6,2,6]
lambda_nums2 = [3,9,4,6]

lambda_list = list(map(lambda num1, num2: num1 * num2, lambda_nums, lambda_nums2))
print(lambda_list)
```

## Nested Statements and Scope

When a variable is declared globally, functions cannot change the value of the variable unless prefixed with “global”. They can only change the value of the variabel **locally**.

```python
x = 50 # Global x

#----------------------------------------------------------------
# Reassigning Locally
def my_func():
    global x #everything that happens to x inside here affects the one globally.
    print(f"X is {x}") # x is 50
    
    x = 200
    print(x) # returns 200

my_func()
print(f"X is now {x}") # x is still 50

#----------------------------------------------------------------
# Reassigning Globally
def my_func():
    global x #everything that happens to x inside here affects the one globally.
    print(f"X is {x}") # x is 50
    
    x = 200

my_func()
print(f"X is now {x}") # x is 200
```