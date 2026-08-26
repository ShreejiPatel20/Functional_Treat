# Data Analyzer and Transformer Program

## Overview

The **Data Analyzer and Transformer Program** is a menu-driven Python program for working with a list of numerical data.

It demonstrates several important Python programming concepts, including:

- Lists and user input
- Built-in functions
- `*args` and `**kwargs`
- Recursion
- Lambda functions
- `filter()`
- Sorting
- Functions that return multiple values
- A `while` loop and menu-based program flow

The program allows the user to enter data and then perform different operations on that data.

---

## Features

### 1. Input Data

The program asks the user to enter numbers separated by spaces.

Example:

```text
Enter data for a 1D array (separated by spaces): 34 12 56 78 43 21 90
```

The values are stored in a Python list.

---

### 2. Display Data Summary

This option displays basic information about the entered data:

- Total number of elements
- Minimum value
- Maximum value
- Sum of all values
- Average value

The program uses Python built-in functions such as:

- `len()`
- `min()`
- `max()`
- `sum()`

Example result:

```text
Data Summary:
-Total_elements:7
-Minimum_value:12
-Maximum_value:90
-Sum_of_all_values:334
-Average_value:47.71
```

---

### 3. Calculate Factorial

This option calculates the factorial of a number using **recursion**.

For example:

```text
5! = 5 × 4 × 3 × 2 × 1 = 120
```

The program uses the `factorial()` function, which calls itself until it reaches the base case.

Example:

```text
Enter a number to calculate its factorial: 5
Factorial of 5 is: 120
```

---

### 4. Filter Data by Threshold

This option filters the entered data based on a threshold value.

The program uses:

- `filter()`
- A `lambda` function

For example, if the threshold is `50`, only values greater than or equal to `50` are displayed.

Example:

```text
Enter a threshold value to filter out data above this value: 50
Filtered Data (values>=50):
56, 78, 90
```

---

### 5. Sort Data

This option allows the user to sort the data in either:

1. Ascending order
2. Descending order

The program uses Python's `sorted()` function.

Example:

```text
Sorted Data (Ascending):
[12, 21, 34, 43, 56, 78, 90]
```

---

### 6. Display Dataset Statistics

This option calculates and displays:

- Minimum value
- Maximum value
- Total/sum of values
- Average value

The `calculate_stats()` function returns multiple values, which are then stored in separate variables.

Example:

```text
Dataset Statistics:
- Minimum value: 12
- Maximum value: 90
- Sum of all values: 334
- Average value: 47.71
```

---

### 7. Exit Program

Selecting option `7` exits the program.

The program displays:

```text
Thank you for using the Data Analyzer and Transformer Program. Goodbye!
```

---

## Program Structure

The main functions used in the program are:

| Function | Purpose |
|---|---|
| `main()` | Displays the menu and controls the program flow |
| `input_data()` | Takes numerical data from the user |
| `show_args()` | Demonstrates the use of `*args` |
| `print_summary()` | Displays key-value information using `**kwargs` |
| `display_summary()` | Displays basic data summary |
| `factorial()` | Calculates factorial using recursion |
| `filter_data()` | Filters values using `filter()` and `lambda` |
| `sort_data()` | Sorts data in ascending or descending order |
| `calculate_stats()` | Calculates and returns multiple statistics |
| `display_stats()` | Displays the calculated dataset statistics |

---

## Concepts Demonstrated

### Built-in Functions

The program demonstrates commonly used Python functions such as:

```python
len()
min()
max()
sum()
sorted()
```

### Recursion

The factorial calculation uses a function that calls itself:

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

### Lambda Function

The filtering operation uses a lambda function:

```python
lambda x: x >= threshold
```

### Variable-Length Arguments

The program also contains examples of:

```python
def show_args(*args):
```

and

```python
def print_summary(**kwargs):
```

These demonstrate how Python functions can accept a variable number of arguments.

### Return Multiple Values

The `calculate_stats()` function returns four values:

```python
return minimum, maximum, total, avg
```

These values are then assigned to separate variables.

---

## How to Run

### Requirements

You need:

- Python 3.x
- A Python editor or IDE such as VS Code, PyCharm, IDLE, or Jupyter-compatible environment

### Steps

1. Save the Python program as a `.py` file.
2. Open a terminal in the folder containing the file.
3. Run:

```bash
python "Functional Treat.py"
```

4. Select an option from the main menu.
5. Follow the instructions displayed by the program.

---

## Example Input

```text
34 12 56 78 43 21 90
```

## Example Results

For the sample data above:

| Statistic | Result |
|---|---:|
| Total Elements | 7 |
| Minimum | 12 |
| Maximum | 90 |
| Sum | 334 |
| Average | 47.71 |

For a factorial input of `5`:

```text
Factorial of 5 is: 120
```

For a threshold of `50`:

```text
56, 78, 90
```

Ascending sorting produces:

```text
[12, 21, 34, 43, 56, 78, 90]
```

---

## Important Note

The program expects numerical input when entering the dataset. The data should be entered as integers separated by spaces.

Example:

```text
10 25 30 45 60
```

The program should be run from the beginning so that data is entered before using the summary, filtering, sorting, or statistics options.

---

## Learning Objectives

This project helps demonstrate how different Python concepts can be combined to create a useful command-line application.

After completing this project, you can understand how to use:

- Functions
- Lists
- Loops
- Conditional statements
- Built-in functions
- Recursion
- Lambda functions
- `filter()`
- Sorting
- `*args` and `**kwargs`
- Multiple return values
- Menu-driven programs
