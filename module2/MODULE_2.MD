# Module 2: Fundamental Operators

## Module Description
This module contains six assignments aimed at practicing Python's fundamental operators.

### Assignment 1: Goals and Objectives. Program Execution Flow. How the Interpreter Shows Variables.
- **[Solution](./path/to/assignment1)**
- **Description:** 
  1. Run the project by clicking on the debug icon (bug) to the right of the project run button.
  2. Observe the result of the program in the console.
  3. Use Step Over to proceed to the next step of the program execution.
  4. Observe the console and the flow of the program execution.
  5. Attach a screenshot of the written code.

### Assignment 2: Homework on "Conditional Constructs. If, Elif, Else Operators."
- **[Solution](./path/to/assignment2)**
- **Description:** **Task "Are All Equal?"**
  - The program receives 3 integers as input and assigns them to variables `first`, `second`, and `third` respectively.
  - Write a conditional construct (using if, elif, else) that outputs the number of equal numbers among the three entered.
    1. If all numbers are equal, output 3.
    2. If at least 2 out of the 3 numbers are equal, output 2.
    3. If there are no equal numbers, output 0.

### Assignment 3: Task "Zeroes Are Nothing, Negatives Are Unacceptable!"
- **[Solution](./path/to/assignment3)**
- **Description:** 
  - Given a list of numbers: `[42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]`, 
  you need to write only positive numbers from this list until you encounter a negative number or the list ends.
  - **Steps:**
    1. Assign the initial list to the variable `my_list`.
    2. Write a while loop with conditions corresponding to the task.
    3. Use break/continue operators in the loop according to the task conditions.

### Assignment 4: Homework on "For Loop. List Elements. Useful Functions in a Loop."
- **[Solution](./path/to/assignment4)**
- **Description:** **Task "It's Not That Simple":**
  - Given a list of numbers: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]`
  - Create a second list `primes` containing only prime numbers from this list.
  - Create a third list `not_primes` containing all non-prime numbers.
  - Output the lists `primes` and `not_primes` to the console.
  - **Steps:**
    1. Create empty lists `primes` and `not_primes`.
    2. Iterate over the `numbers` list using a for loop.
    3. Use another nested for loop to find divisors for the number from the first loop.
    4. Mark the number as prime using a variable `is_prime`, setting it to True before the check.
    5. During the check, append the numbers from `numbers` to `primes` or `not_primes` lists 
    based on the value of `is_prime` after the check (True - in `primes`, False - in `not_primes`).
    6. Output the lists `primes` and `not_primes` to the console.

### Assignment 5: Homework on "Functions in Python. Function with Parameters."
- **[Solution](./path/to/assignment5)**
- **Description:** **Task "Matrix in Reality":**
  - Write a function `get_matrix` with three parameters `n`, `m`, and `value` 
  that creates a matrix (nested list) of size `n` rows and `m` columns, filled with values `value`, 
  and returns this matrix as a result.
  - **Steps:**
    1. Declare the function `get_matrix` with parameters `n`, `m`, and `value`.
    2. Create an empty list `matrix` inside the function `get_matrix`.
    3. Write the first (outer) for loop for the number of rows in the matrix, `n` repetitions.
    4. In the first loop, add an empty list to the `matrix`.
    5. Write the second (inner) for loop for the number of columns in the matrix, `m` repetitions.
    6. In the second loop, fill the previously added empty list with values `value`.
    7. After all loops, return the value of the variable `matrix`.
    8. Output the result of the `get_matrix` function to the console.

### Additional Assignment: Practical Exercise on "Fundamental Operators"
- **[Solution](./path/to/additional_assignment)**
- **Description:**
  **Task "Ancient Cipher Too Complex":**
  - You went on a journey to an uninhabited island and, of course, on one of your forays into the jungle, 
  you fell into a trap set by a local tribe. 
  To your surprise, the tribe had good mathematicians who were also creative. 
  You realized this when, after wandering for a long time, 
  you came across gates (the way out of the trap) with two stone inserts for numbers. 
  - In the first insert, the stones with the number constantly changed randomly from 3 to 20, 
  while the second insert was always empty.
  - Fortunately for you, next to the less successful and now silent travelers, 
  there was a papyrus that had the rules for solving this "puzzle" written on it (too bad they figured it out too late).
  - You need to write pairs of numbers in the second insert 
  so that the number from the first insert is divisible by the sum of their values without a remainder.
  - **Example of divisibility (no remainder):**
    1 + 2 = 3 (sum of the pair)
    9 / 3 = 3 (exactly 3 without a remainder)
    9 is divisible by 3 without a remainder (9 is a multiple of 3)
  - **Example 1:**
    9 - the number from the first insert
    1218273645 - the required password (1 and 2, 1 and 8, 2 and 7, 3 and 6, 4 and 5 - pairs; 
    the number 9 is divisible by the sum of each pair)
  - **Example 2:**
    11 - the number from the first insert
    11029384756 - the required password (1 and 10, 2 and 9, 3 and 8, 4 and 7, 5 and 6 - pairs; the number 11 is divisible by the sum of each pair)
