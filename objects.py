from classes import Animal, Eagle, Employee, Salary, CoffeeShop


dog = Animal("Charlie")
eagle = Eagle("Dave")

s = Salary(150000, 15000)
e = Employee("David", s)

shop = CoffeeShop("bellum Cafe")
shop.add_to_menu("Espresso", "$2")
shop.add_to_menu("Latte", "$3")