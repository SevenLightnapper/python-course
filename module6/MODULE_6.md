# Module 6: Class Inheritance

## Module Description
This module covers inheritance in Python, focusing on building class hierarchies, method overriding, 
multiple inheritance, and advanced class design principles.

### Assignment 1: Homework on "Why Inheritance Is Needed"
- **[Solution](./hw1)**
- **Description:** 
  **Task "Edible or Inedible":** 
  - Implement an animal kingdom hierarchy using inheritance. Create parent classes `Animal` and `Plant`, 
    and child classes `Mammal`, `Predator`, `Flower`, and `Fruit`. 
    Include methods for animals to eat plants, where animals get fed if the plant is edible and die if it is not.

### Assignment 2: Homework on "Accessing Parent Properties. Overriding Properties"
- **[Solution](./hw2)**
- **Description:** 
  **Task "Cannot Change, Only Get":** 
  - Implement a `Vehicle` class and its subclass `Sedan`. 
    The `Vehicle` class should have private attributes for model, engine power, 
    and color, which can be retrieved but not directly modified. 
    The `Sedan` class should inherit these properties and include an additional passenger limit.

### Assignment 3: Homework on "Multiple Inheritance"
- **[Solution](./hw3)**
- **Description:** 
  **Task "Mythical Inheritance":** 
  - Create classes `Horse`, `Eagle`, and `Pegasus`. `Pegasus` should inherit from both `Horse` and `Eagle`, 
    and include methods for both running and flying, as well as returning its current position and sound.

### Additional Assignment: Practical Exercise on "Class Inheritance"
- **[Solution](./hw4)**
- **Description:** 
  **Task "They All Look So Alike":** 
  - Implement a hierarchy of 2D and 3D geometric shapes using classes. Create a base class `Figure`, 
    and subclasses `Circle`, `Triangle`, and `Cube`. Each shape should have methods for managing dimensions, 
    colors, and calculating area or volume.
