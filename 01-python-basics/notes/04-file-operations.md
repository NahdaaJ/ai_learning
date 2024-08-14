# File Operations

## `.txt` Files

### Opening a File

Before any operations on a file, you need to open it. After use, you need to close the file. This can either be done like this:

```python
file = open('filename.txt', 'mode')

# File logic

file.close()
```
Or like this (this automatically closes it):

```python
with open('example.csv', 'mode') as file:
    # Logic
```

`filename.txt` → this is the path to the file you want to open .

`mode` → this is the mode in which you want to open the file.

| Mode | Descriptionr | If the file does not exist…. |
| --- | --- | --- |
| r | `Read` (default mode). Opens the file for reading.  | Raises an error. |
| w | `Write`. Opens the file for writing. If the file exists, it will be overwritten.  | File is created. |
| a | `Append`. Opens the file for appending data.  | File is created. |
| r+ | `Read and Write`. Opens the file for both reading and writing. |  |

### Reading from a File

The file has to be opened in `r` mode. To read data from a file, you can use several methods:

| Method | Description |
| --- | --- |
| `read()` | Reads the entire content of the file. |
| `readline()` | Reads one line at a time. |
| `readlines()` | Reads all lines and returns a list where each element is a line from the file. |

```python
# Open file for reading
file = open('example.txt', 'r')

# Read the entire file
content = file.read()
print(content)

# Close the file
file.close()

```

### Writing to a File

To write data to a file, you can use:

| Method | Description |
| --- | --- |
| `write()` | Writes a string to the file. |
| `writelines()` | Writes a list of strings to the file. |

```python
# Open file for writing
file = open('example.txt', 'w')

# Write a string to the file
file.write("Hello, World!\n")

# Write multiple lines
file.writelines(["This is line 1\n", "This is line 2\n"])

# Close the file
file.close()

```

### Appending to a File

If you want to add content to an existing file without overwriting it, you can open the file in append mode.

```python
# Open file in append mode
file = open('example.txt', 'a')

# Append text to the file
file.write("Appending a new line\n")

# Close the file
file.close()
```

### Using `with` Statement (Context Manager)

It's a good practice to use the `with` statement when working with files. This ensures that the file is properly closed after its suite finishes, even if an exception is raised.

Example:

```python
pythonCopy code
# Using with statement to automatically close the file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

```

---

## `.csv` Files

### Importing the `csv` Module

To work with csv files, you have to import the `csv` module at the top of the file.

```python
import csv
```

| Methods | Description |
| --- | --- |
| `csv.reader()` | Reads the content of the csv file row by row. Can be casted into a list. |
| `writer = csv.writer()` `writer.writerow()` OR `writer.writerows()` | Used to write rows to the csv file. Can be written row by row or multiple rows at a time. |
| `csv.DictReader()` | Sometimes, it’s more convenient to work with CSV files as dictionaries where the first row contains the column headers. |
| `writer = csv.DictWriter(file, fieldnames=fieldnames)` | You can also write CSV files using dictionaries, where you specify the fieldnames (column headers) first. |
| `reader = csv.reader(file, delimiter=';')` | If your CSV file uses a different delimiter (e.g., semicolon ; or tab \t), you can specify the delimiter when creating the reader or writer. |

### Using DictReader and DictWriter

```python
import csv

# Open the CSV file for reading
with open('example.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Each row is a dictionary with column names as keys
    for row in reader:
        print(row)
```

```python
import csv

# Data to be written to the CSV file
data = [
    {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
]

# Open the CSV file for writing
with open('example.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Write the header (column names)
    writer.writeheader()
    
    # Write the data
    writer.writerows(data)
```