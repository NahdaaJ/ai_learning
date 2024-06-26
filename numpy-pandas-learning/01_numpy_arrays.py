# Array creation and properties -----------------------------------------
import numpy as np

sales = [[0, 5, 155, 0, 518],
         [0, 1827, 616, 317, 325]]

sales_array = np.array(sales)

print("--------------------------")

print(f"""A NumPy array has type {type(sales_array)}.
- Number of Dimensions: {sales_array.ndim}
- Size of Array: {sales_array.shape}
- Total Number of Elements: {sales_array.size}
- Data Type of Elements: {sales_array.dtype}

{sales_array}

Transpose
{sales_array.T}""")

# Creating an array with range 0 to 4 -----------------------------------------
print("--------------------------")
range_array = np.array([range(5), range(5)])
print(f"\nArray using range() \n{range_array+1}")
print(f"\nArray + 1 \n{range_array+1}")
print(f"\nArray x 7 \n{range_array*7}")
