# Statements

Statements are used when we want the code to execute certain code, based on when certain conditions are met.

`break` → breaks out of the closest enclosing loop.

`continue` → ignores the rest of the code block and begins the next iteration of the loop.

`pass` → does nothing.

## `If`, `Elif`, and `Else`

IF a condition is met, do action A, else do action B.

If a condition 1 is met, do action A, else if condition 2 is met, do action B, else do action C.

```python
my_age = 24

if my_age < 18:
	print("You are a baby!")
elif my_age > 18:
	print("You are a granny!")
else:
	print("You're an adult now!")
```

## `For` Loops

Used to execute a block of code for every iteration.

```python
my_family = ["Trung", "Ammu", "Zayn", "Nael"]

for (i = 0 ; i < len(my_family) ; i++ ):
	print(f"I love {my_family[i]}!")
	

# Can do this for strings as well.
for member in my_family:
	print(f"I love {member}!")
	
	
my_list = [(1,2,3) , (4,5,6) , (7,8,9)]

for a,b,c in my_list:
	print(b)
```

## `While` Loops

While this condition is true, execute this block of code.

```python
x = 0

while x < 5:
	print(f"Current number: {x}")
	x += 1
	
#optional
else:
	print("x is not less than 5.")
```

## Useful Operators

| Operator | Syntax | Description |
| --- | --- | --- |
| Range | `range(start, stop, step)` | Creates a specified number sequence. Can convert to a list using list() . |
| Enumerate | `enumerate(my_object)`| Returns tuples, associating a number with the item. It can take in any iterable object and returns an index counter with the associated element. |
| Zip | `zip(list1, list2)` | Pairs up the items in two or more lists. |
| In | `item in my_list` | Returns true or false, checks for item in iterable object. |
| Min/Max | `max(my_nums) min(my_nums)` | Returns the min/max value of a numerical iterable object. |
| Shuffle | `from random import shuffle` `shuffle(my_list)` | Needs to be imported. Used to shuffle/scramble a list. CANNOT BE USED TO CREATE A VARIABLE. It shuffles the list you provided it. |
| Random Integer | `from random import randint` `randint(start, stop)` | Used to generate a random integer between the specified numbers. Includes the starting number but not the stop number. |
| User Input | `input()` `input(”How are you?”)` | Use this to get input from the users keyboard. |

## List Comprehensions

Shorthand ways of working with lists in python. Generally shouldn’t do this, as it decreases readability.

Instead of:

```python
for letter in my_string:
	my_list.append(letter)
```

Write:

```python
my_list = [letter for letter in my_string]
my_list = [num for num in range(1,10)
my_list = [num*2 for num in range(1,10)
my_list = [x for x in range (0,11) if x%2 ==0)]
fahrenheit = [(3*temp) for temp in celcius]
```