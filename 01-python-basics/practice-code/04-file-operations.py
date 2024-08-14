import csv

# Creates file or rewrites over existing.
with open('../test-files/test.txt', 'w') as file:
    file.write("Hello World!")
    
# Creates file or adds content to the end.    
with open('../test-files/test.txt', 'a') as file:
    file.write("\nI am Nahdaa!")
    
with open('../test-files/test.txt', 'r') as file:
    read = file.read()
    readline = file.readline()
    readlines = file.readlines()
    print("read", read)
    
    # Doesnt work? No output
    print("readline")
    for line in readline:
        print(line)
        
    # Doesnt work? No output
    print("readlines")
    for line in readlines:
        print(line)
    
print("\n\n\n\n")

# -------------------------------------------------------------------------------
# CSV using csv.writer(file) and csv.reader(file)
data1 = [
    ['Name', 'Age', 'City'],
    ['Nahdaa', '24', 'London'],
    ['Nael', '4', 'Manchester'],
    ['Zayn', '9', 'Manchester'],
]

data2 = [
    ['Trung', '28', 'London'],
]

with open('../test-files/test-csv.csv', 'w', newline="") as file:
    writer = csv.writer(file)
    
    # for row in data1:
    #     writer.writerow(row)
    
    writer.writerows(data1)
    
with open('../test-files/test-csv.csv', 'a', newline="") as file:
    writer = csv.writer(file)
    
    writer.writerows(data2)
    
with open('../test-files/test-csv.csv', 'r', newline="") as file:
    reader = csv.reader(file)

    # using for
    print("FOR-------------------------------------")
    for row in reader:
        print (row)
        
    # pointing to the start of the file again
    file.seek(0)
        
    print("List-------------------------------------")
    # using list
    data = list(reader)
    print(data)

print("\n\n\n\n")

# -------------------------------------------------------------------------------
# CSV using csv.DictWriter and csv.DictReader

dict_data1 = [
    {"Name": "Nahdaa", "Age": 24, "City": "London"},
    {"Name": "Nael", "Age": 4, "City": "Manchester"},
    {"Name": "Zayn", "Age": 9, "City": "Manchester"}
]

dict_data2 = [
    {"Name": "Trung", "Age": 28, "City": "London"}
]

with open('../test-files/test-csv2.csv', 'w', newline="") as file:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(file, fieldnames = fieldnames )
    
    writer.writeheader() # only for writing
    writer.writerows(dict_data1)
    
with open('../test-files/test-csv2.csv', 'a', newline="") as file:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(file, fieldnames = fieldnames )
    
    writer.writerows(dict_data2)
    
with open('../test-files/test-csv2.csv', 'r', newline="") as file:
    reader = csv.DictReader(file)
    
    # Each row is a dictionary
    for row in reader:
        for key,value in row.items():
            print(f"{key}: {value}")
        print("\n")