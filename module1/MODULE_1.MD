# Module 1: Basic Data Structures

## Module Description
This module contains seven assignments aimed at practicing Python's basic data structures.

### Assignment 0: Practical Exercises on "Basic Data Structures"
- **[Solution](./hw0)**
- **Description:** This assignment consists of five tasks:
  1. **Word Length:** Write an arbitrary string into the variable `a`. 
  Then, calculate the length of the string and display the result.
  2. **Sums and Differences:** Write two integers into the variables `first` and `second`. 
  Calculate their sum and difference, store them in the variables `summa` and `diff` respectively, and display these values.
  3. **Arithmetic Mean:** Write three numbers into the variables `first`, `second`, and `third`. 
  Calculate their arithmetic mean and store it in the variable `mean`. Display the value of `mean`.
  4. **Simple Strings:** Create two variables `first_string` and `second_string` with the strings "Tuesday" and "Monday". 
  Display the strings so that "Monday" comes before "Tuesday" with a comma and a space between them ("Monday, Tuesday").
  5. **Complex Formula:** Write three numbers into the variables `a`, `b`, and `c`. 
  Create a variable `f` to store the result of the expression `(a * b) + (a * c)`. 
  Raise the result to the third power and divide it by two. Display the final result.

### Assignment 1: Practical Exercises on "Strings and String Indexing"
- **[Solution](./hw1)**
- **Description:** 
  1. Assign any string to the variable `example`.
  2. Display the first character of this string.
  3. Display the last character of this string using a negative index.
  4. Display the second half of this string.
  5. Display this string in reverse order.
  6. Display every second character of this string.

### Assignment 2: Practical Exercises on "Variables in PyCharm"
- **[Solution](./hw2)**
- **Description:** 
  1. Create variables to store the following data:
     - Number of completed assignments (value: 12)
     - Number of hours spent (value: 1.5)
     - Course name (value: 'Python')
     - Time per assignment (calculate using the first two variables)
  2. Display the following string using these variables: 
  "Course: Python, total tasks: 12, hours spent: 1.5, average time per task: 0.125 hours."

### Assignment 3: Practical Exercises on "Dynamic Typing"
- **[Solution](./hw3)**
- **Description:**
  1. Create a variable `name` and assign it a string value.
  2. Display the value of `name`.
  3. Create a variable `age` and assign it an integer value.
  4. Display the value of `age`.
  5. Add a new value to `age` and display the updated value.
  6. Create a variable `is_student` and assign it a boolean value.
  7. Display the value of `is_student`.

### Assignment 4: Practical Exercises on "Program Organization and String Methods"
- **[Solution](./hw4)**
- **Description:**
  1. Organize a program:
     - Create a variable `my_string` and assign it a string value using input().
     - Display the number of characters in the input string.
  2. Using string methods, perform the following actions:
     - Display `my_string` in uppercase.
     - Display `my_string` in lowercase.
     - Remove all spaces from `my_string`.
     - Display the first character of `my_string`.
     - Display the last character of `my_string`.

### Assignment 5: Practical Exercises on "Immutable and Mutable Objects, Tuples and Lists"
- **[Solution](./hw5)**
- **Description:**
  1. **Define Variables of Different Data Types:**
     - Create a variable `immutable_var` and assign it a tuple with several elements of different data types.
     - Display the tuple `immutable_var`.
  2. **Change Variable Values:**
     - Attempt to modify the elements of the tuple `immutable_var`. Explain why tuple elements cannot be modified.
  3. **Create Mutable Data Structures:**
     - Create a variable `mutable_list` and assign it a list with several elements.
     - Modify the elements of the list `mutable_list`.
     - Display the modified list `mutable_list`.

    #### Additional Tasks
    
    **5.1 Task: Modifying Nested Lists**
    - **[Solution](./hw5/extra/task1)** 
    - **Description:** Write a function that takes a list of lists of numbers and multiplies each element by 2. 
    Show how this function works with mutable objects.
    
    **5.2 Task: Copying Mutable Objects**
    - **[Solution](./hw5/extra/task2)** 
    - **Description:** Write a function that takes a list and returns a deep copy of it, where all nested lists are also copied.
    
    **5.3 Task: Reversing Words in a Sentence**
    - **[Solution](./hw5/extra/task3)**
    - **Description:** Write a function that takes a sentence and returns a new sentence where each word is reversed, 
    but the order of words is preserved.
    
    **5.4 Task: Character Frequency**
    - **[Solution](./hw5/extra/task4)**
    - **Description:** Write a function that takes a string and returns a dictionary 
    where the keys are the characters in the string, and the values are their frequencies.
    
    **5.5 Task: Anagram Check**
    - **[Solution](./hw5/extra/task5)**
    - **Description:** Write a function that takes two strings and checks if they are anagrams 
    (contain the same characters in different orders).
    
    **5.6 Task: Sorting a List of Tuples**
    - **[Solution](./hw5/extra/task6)**
    - **Description:** Write a function that takes a list of tuples, where each tuple contains two numbers, 
    and returns the list sorted by the second number in each tuple.

### Assignment 6: Practical Exercises on "Dictionaries and Sets"
- **[Solution](./hw6)**
- **Description:**
  1. **Working with Dictionaries:**
     - Create a variable `my_dict` and assign it a dictionary with several key-value pairs (e.g., Name (str) - Birth Year (int)).
     - Display the dictionary `my_dict`.
     - Display one value for an existing key and one for a non-existing key without causing an error.
     - Add two more arbitrary key-value pairs to the dictionary `my_dict`.
     - Remove one pair by an existing key from the dictionary `my_dict` and display the value.
     - Display the dictionary `my_dict`.
  2. **Working with Sets:**
     - Create a variable `my_set` and assign it a set containing different data types with duplicate values.
     - Display the set `my_set` (should show only unique values).
     - Add two arbitrary elements to the set `my_set` that are not already in it.
     - Remove one element from the set `my_set`.
     - Display the modified set `my_set`.

### Additional Assignment: Practical Exercise on "Basic Data Structures"
- **[Solution](./hw7)**
- **Description:**
  **Task "Average Grade":**
  Solve a real-life problem where school teachers are tired of manually calculating the average grade of each student, 
  so you need to automate this process:
  - **Input Data:**
    1. A list: `grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]`
    2. A set: `students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}`

    - The `grades` list contains lists of grades for each student in alphabetical order.
      For example: 'Aaron' - `[5, 3, 3, 5, 4]`
    - The `students` set contains an unordered sequence of names of all students in the class.

  - **Task:** Write a program that creates a dictionary using `grades` and `students`, 
  where the key will be the student's name and the value will be their average grade.
