import classes
from objects import dog, eagle, e, shop

print(dog.speak())

print(eagle.speak())

# testing composition
print(e.salary.pay)
print(e.salary.bonus)

# inspecting salary
print(type(e.salary))
vars(e.salary)

# for bellum coffee shop
shop.serve("Espresso")  # Output: Serving Espresso for $2!
shop.serve("Tea")       # Output: Sorry, Tea is not available.