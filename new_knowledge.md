# Points
- `__init__` is used to instatiate an object of a class to a _specific_ initial state
- classes can be created without init. But all attributes of any class created without init will be included manually, and no methods can be added to it outside the class definition

# miscellanous
- In Python, when you assign multiple values to a variable using a comma-separated list,  without parentheses, like `var = 3, 4, 7, 9`, it automatically creates a **tuple** in the interpreter's memory. This is because the comma is the actual operator that generates a tuple, and the parentheses are optional unless needed for clarity or when the tuple is empty.