# Module 9: Functional programming

## Module Description
This module introduces functional programming concepts in Python, 
including lambda functions, closures, iterators, generators, decorators, and comprehensions.

### Assignment 1: Homework on "Introduction to Functional Programming"
- **[Solution](./hw1)**
- **Description:** 
  **Task "Apply All Functions at Once":** 
  - Implement the `apply_all_func` function that takes a list of numbers and an arbitrary number of functions, 
    applying each function to the list 
    and returning a dictionary with function names as keys and their results as values.

### Assignment 2: Homework on "List and Dictionary Comprehensions"
- **[Solution](./hw2)**
- **Description:** 
  - Create list and dictionary comprehensions to filter and pair elements based on string lengths, 
    and to create a dictionary with string lengths for strings with an even length.

### Assignment 3: Homework on "Generator Expressions"
- **[Solution](./hw3)**
- **Description:** 
  - Implement generator expressions to calculate differences in string lengths from two lists 
    and to compare string lengths at the same positions without using `zip`.

### Assignment 4: Homework on "Creating Functions on the Fly"
- **[Solution](./hw4)**
- **Description:** 
  **Task "Functional Diversity":**
  - Write a lambda function to compare character matches in two strings. Implement a closure 
    that returns a function for writing multiple data types to a file. 
    Also, create a class with the `__call__` method that randomly returns words from a collection.

### Assignment 5: Homework on "Iterators"
- **[Solution](./hw5)**
- **Description:** 
  **Task "Range Is Simple":**
  - Create an iterator class that behaves similarly to Python's `range()` function but allows for step validation. 
    Implement custom error handling for invalid steps.

### Assignment 6: Homework on "Generators"
- **[Solution](./hw6)**
- **Description:** 
  - Write a generator function `all_variants` that returns all subsequences of a given string during iteration.

### Assignment 7: Homework on "Decorators"
- **[Solution](./hw7)**
- **Description:** 
  - Implement a decorator function that checks whether the result of another function (which sums three numbers) 
    is a prime number, printing "Prime" or "Composite" based on the result.
