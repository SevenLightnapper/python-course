# Module 4: Modules and packages. Namespaces and scopes

## Module Description
This module focuses on understanding and utilizing Python modules and packages, 
as well as practicing namespaces in functions.

### Assignment 1: Homework on "Modules and Packages"
- **[Solution](./hw1)**
- **Description:** 
  **Task "How to Divide?":** 
  - Create two modules, `fake_math` and `true_math`, 
  each containing a `divide` function that handles division in different ways.
    - `fake_math.divide`: Returns an error message when dividing by zero.
    - `true_math.divide`: Returns infinity when dividing by zero (using `math.inf`).
  - Import these functions into a main module using the `as` keyword to avoid name conflicts, 
  and test them by passing values, including zero as the divisor.

### Assignment 2: Homework on "Namespaces"
- **[Solution](./hw2)**
- **Description:** 
  **Task "Function Scope":**
  - Create a function `test_function` and define an inner function `inner_function` within it that prints a message. 
Call `inner_function` within `test_function` and test whether `inner_function` can be called outside of `test_function`.
