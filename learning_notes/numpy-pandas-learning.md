# NumPy Arrays

**NumPy arrays** are fixed-size containers of items that are more efficient thatn Python lists or tuples for data processing.

- They only store a single data type.
- They can be one dimensional or multi-dimensional.
- Array elements can be modified, but the array size cannot change.

## Properties

- `.ndim` → number of dimensions in array
- `.shape` → size of array for each dimension
- `.size` → total number of elements in array
- `.dtype` → data type of elements in array

**Example of Use:**
```
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
```

  ## Array Creation
- `np.array([])` → creates a basic NumPy array

  ## Array Operations
- `.T` → tranposes the array
