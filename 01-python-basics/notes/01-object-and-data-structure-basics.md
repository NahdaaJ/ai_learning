# Object and Data Structure Basics

**Mutable** - Can be changes after creation.

**Immutable** - Cannot be changed after creation.

## Data Types

Python uses dynamic typing, meaning you can reassign variables to different data types.

| Data Type Name | Syntax | Description |
| --- | --- | --- |
| lists | [ ] | A list is an ordered collection of items that can be of different types. Lists are mutable, meaning that their elements can be changed after the list has been created. |
| dictionaries | { ” “ : }  | A dictionary is an unordered collection of key-value pairs. Each key is unique, and values can be of any type. Dictionaries are mutable. |
| tuples | ( ) | Definition: A tuple is an ordered collection of items that can be of different types. Tuples are immutable, meaning that once they are created, their elements cannot be changed. |
| sets | { } or set() | A set is an unordered collection of unique elements. Sets are mutable, but they cannot contain mutable elements like lists or dictionaries. Elements can be added or removed, but the elements themselves can’t change (cannot contain lists or dictionaries). |

## Python Numbers

| Operator | Syntax | Description |
| --- | --- | --- |
| modulo | % | Used to find the remainder after division. |
| power | ** | Used to calculate numbers to a power (e.g. $2^3$) |

## Strings

Strings themselves are **immutable**.

| Property Name | Syntax | Description |
| --- | --- | --- |
| slicing | `[ start : stop : step ]` | Used to index/slice sections of the string. Does NOT include stop index, includes start index. |
| new line | `\n` | Inserts a new line. |
| tab | `\t` | Inserts a tab. |
| length | `len()` | Returns integer length of string. |
| add strings | `+` | You can add strings to other strings. |
| multiply strings | `*` | You can multiply strings by integers. |
| uppercase string | `[string_var].upper()` | Uppercases all letters. |
| lowercase string | `[string_var].lower()` | Lowercases all letters. |
| split string to list of strings | `[string_var].split()` `[string_var].split("i")` | By default, splits a string using spaces. Split character can be specified. |
| formatting strings | `.format('hello', 'world')` | Used to insert variables into a string. |
| f strings (formatted string literals) | `f"Hello {name}"` | Used to insert variables into a string. |


## Lists

Can have multiple data types. You can add lists together. Lists are mutable, you can change the elements of the list using `=` .

| Property Name | Syntax | Description |
| --- | --- | --- |
| Length of List | `len(my_list)` | Returns the integer length of the list. |
| Indexing | `my_list[int]` | Returns the element at the specified index. |
| Slicing | `my_list[int:]` | Returns the list of elements from the specified index onwards. |
| Append | `my_list.append(element)` | Adds the new element to the end of the list. |
| Pop | `my_list.pop()` | Removes and returns the last element in the list by default. You can specify index to pop that specific element. |
| Sort | `my_list.sort()` | Sorts alphabetically or numerically. |
| Reverse | `my_list.reverse()` | Reverses the order of the list. |

## Dictionaries

Dictionaries are unordered mappings for storing objects. Dictionaries use key-value pairing. Useful for when you don’t know index. Dictionaries are unordered and cannot be sorted. Lists and dictionaries can be nested inside of dictionaries. Dictionaries are mutable, you can change the values at the keys.

```python
my_dictionary = {'key1' : 'value1', 'key2' : 3 }
```

| Method Name | Syntax | Description |
| --- | --- | --- |
| Retrieve Value |`my_dict[’key1’]`| Returns the value associated with the key. |
| Retrieve All Keys | `my_dict.keys()` | Returns a list of keys. |
| Retrieve All Values | `my_dict.keys()` | Returns a list of values. |
| Retrieve Items | `my_dict.items()` | Returns all the key value pairs inside of the dictionary. |

## Tuples

Tuples are similar to lists, except you cannot reassign elements inside the tuple. Uses ().

| Method Name | Syntax | Description |
| --- | --- | --- |
| Length of Tuple | `len(my_tuple)` | Returns the integer length of the tuple. |
| Indexing | `my_tuple[int]` | Returns the element at the specified index. |
| Count | `my_tuple.count(element)` | Returns the number of times the element appears in the tuple. |
| Index | `my_tuple.index(element)` | Returns the index of the element if it exists in the tuple. |

## Sets

Sets are unordered collections of unique elements. An element can only appear once.

| Method Name | Syntax | Description |
| --- | --- | --- |
| Add | `my_set.add(element)` | Adds an element to the end of your set. |
| Convert to Set | `set(my_list)` | Converts the list into a set, removes all duplicate elements. |