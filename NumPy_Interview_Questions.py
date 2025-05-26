#Basic NumPy Interview Questions
'''
Use these basic interview questions to check your understanding of NumPy fundamentals. They are great warmups and starter points for ensuring you know NumPy’s functionality and purpose.

1. What is NumPy, and why is it used in data science?

NumPy is a Python package with many portions built in C/C++ for performance reasons. Its main goal is to make the computation of large data arrays faster and easier in Python.

Its core functionality is as follows:

1. It provides support for large, multi-dimensional arrays and matrices, which are essential for handling large datasets.
2. It offers a comprehensive collection of mathematical functions to operate on these arrays efficiently, enabling fast computations on large datasets.
3. NumPy's vectorized operations allow for the efficient execution of complex mathematical operations.
4. It forms the foundation for many other data science libraries like pandas, scikit-learn, and SciPy, making it a cornerstone of the Python data science ecosystem.
5. NumPy arrays are more memory-efficient than Python lists, which is crucial when working with big data.
'''
'''
2. How do you create a 1D array in NumPy?

Creating a Numpy array is super easy! You simply need to invoke the array() method to create an array object. Understanding how to make 1D arrays will allow you to build out higher n-dimensional NumPy arrays.
'''
import numpy as np
arr = np.array([1, 2, 3, 4, 5])

'''
3. What's the difference between a Python list and a NumPy array?

The main differences between Python lists and NumPy arrays are:

1. Homogeneity: NumPy arrays are homogeneous, meaning all elements must be the same type. Python lists can contain elements of different types.
2. Memory efficiency: NumPy arrays are more memory-efficient because they store data in a contiguous block of memory, unlike Python lists, which store pointers to objects.
3. Performance: NumPy arrays support vectorized operations, making them much faster for numerical computations. Operations are performed element-wise without the need for explicit loops.
4. Functionality: NumPy arrays come with a wide range of mathematical operations and functions that can be applied directly to the array, which is not possible with Python lists.
'''

'''
4. How do you check the shape and size of a NumPy array?

Understanding how to check the shape of a NumPy array is important because, during data processing, you may have an expected final output array size. 

If your result does not meet your expectations, checking the NumPy array shape will allow you to take steps toward resolving those issues.
You can use the shape attribute to get the dimensions of the array and the size attribute to get the total number of elements:
'''

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  # Output: (2, 3)
print(arr.size)   # Output: 6

'''
5. How do you reshape a NumPy array?

Reshaping arrays is a common operation in data preprocessing and feature engineering.
It is crucial for adapting data to various algorithms' input requirements or reorganizing data for analysis. 

You can reshape a NumPy array using the reshape() method or the np.reshape() function.
Here's how:
'''

import numpy as np

# Using reshape() method
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2, 3)
print(reshaped_arr)
# Output:
# [[1 2 3]
#  [4 5 6]]

# Using np.reshape() function
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = np.reshape(arr, (3, 2))
print(reshaped_arr)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]]

 
'''#Intermediate NumPy Interview Questions'''
'''
6. How do you create an array of all zeros or all ones?

Creating arrays filled with zeros or ones is a common requirement in many data science tasks, such as initializing matrices, creating mask arrays, or setting up placeholder data structures. 

To create an array of all zeros or all ones in NumPy, you use the np.zeros() or np.ones() functions:
'''

import numpy as np

# Create a 3x4 array of zeros
zeros_arr = np.zeros((3, 4))
print(zeros_arr)
# Output:
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

# Create a 2x2 array of ones
ones_arr = np.ones((2, 2))
print(ones_arr)
# Output:
# [[1. 1.]
#  [1. 1.]]

'''
7. What is broadcasting in NumPy?

Broadcasting is a key NumPy behavior that allows for efficient operations on arrays of different sizes. 

Simply put, it allows for arithmetic operations between arrays of different sizes by ensuring both arrays have compatible shapes. This is done when NumPy automatically replicates smaller arrays across the larger array so that they have compatible shapes. 

See the following example:
'''

import numpy as np

a = np.array([1, 2, 3])b = np.array([[1], [2], [3]])
print(a + b)
# Output:
# [[2 3 4]
#  [3 4 5]
#  [4 5 6]]

'''
8. How do you find the mean, median, and standard deviation of a NumPy array?

The mean, median, and standard deviation are key descriptive statistics commonly used to understand our data.
NumPy calculates these very easily and has functions specially built for them. 

Knowing these calculations is important for enhancing our ability to utilize NumPy:
'''

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Mean
mean_value = np.mean(arr)
print("Mean:", mean_value)  # Output: 3.0

# Median
median_value = np.median(arr)
print("Median:", median_value)  # Output: 3.0

# Standard deviation
std_value = np.std(arr)
print("Standard deviation:", std_value)  # Output: 1.4142135623730951

'''
9. How can we utilize NumPy to quickly query our numerical data and perform actions based on a boolean statement?

While we think of NumPy’s primary purpose as a calculation package, it also has powerful data-wrangling capabilities. 

NumPy can easily query data through boolean indexing and perform operations based on results. The where() method is particularly useful when we want to make changes to our data based on numerical values.

Assume we have a data frame of exam scores named df and want to categorize the students. A simple np.where() may look like:
'''

df[‘student_cat’] = np.where(df[‘score’] > 80, ‘good’, ‘bad’)

'''
Note that the where() method takes up to 3 inputs: 

The first is the boolean statement of any kind
The second is the result if true
The third is the result if false
'''

'''
10. What is a way to utilize NumPy for something like Mean Squared Error?

NumPy’s ability to work across an entire array at once makes implementing calculations like Mean Squared Error (MSE) simple. 

Because it performs simple operations on an element-by-element basis it easily vectorizes the operation and provides an efficient way of calculating MSE. 

An example of an implementation of MSE in NumPy follows:
'''

# 1. We have two arrays, our prediction, and actual labels
# 2. We take the squared differences and sum them
# 3. We then divide by n, which is the length of the array

n= len(labels)
error = (1/n) * np.sum(np.square(predictions - labels))