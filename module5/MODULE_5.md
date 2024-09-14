# Module 5: Classes and objects

## Module Description
This module focuses on object-oriented programming in Python, covering attributes, methods, 
operator overloading, and class-level versus instance-level attributes.

### Assignment 1: Homework on "Attributes and Methods of an Object"
- **[Solution](./hw1)**
- **Description:** 
  **Task "Developer - Not Just a Coder":** 
  - Implement a `House` class with attributes for the name and number of floors. 
  The class should include a method `go_to` that prints the floor numbers from 1 to the specified floor 
  or an error message if the floor doesn't exist.

### Assignment 2: Homework on "Special Methods of Classes"
- **[Solution](./hw2)**
- **Description:** 
  **Task "Magical Buildings":** 
  - Extend the `House` class to include special methods like `__len__`, which returns the number of floors, 
  and `__str__`, which provides a formatted string representation of the house.

### Assignment 3: Homework on "Operator Overloading"
- **[Solution](./hw3)**
- **Description:** 
  **Task "Operator Overloading":** 
  - Implement comparison operators (`__eq__`, `__lt__`, `__le__`, etc.) 
  for the `House` class to compare buildings by their number of floors. 
  Also, implement the `__add__`, `__radd__`, and `__iadd__` methods to increase the number of floors.

### Assignment 4: Homework on "Class Attributes vs Instance Attributes"
- **[Solution](./hw4)**
- **Description:** 
  **Task "Construction History":** 
  - Add a class-level attribute `houses_history` to track all created house objects. 
  Implement the `__new__` and `__del__` methods to automatically record new houses and log when a house is demolished.

### Additional Assignment: Practical Exercise on "Classes and Objects"
- **[Solution](./hw5)**
- **Description:** 
  **Task "UrTube Platform":** 
  - Implement a set of classes (`User`, `Video`, `UrTube`) to simulate the behavior of a video-sharing platform, 
  including user registration, video uploading, and video watching with age restrictions and playback tracking.
