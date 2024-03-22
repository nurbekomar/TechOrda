# 1 Задача
"""
class Car:
    def __init__(self, brend, model, year):
        self.brend = brend
        self.model = model
        self.year = year

    def description(self):
        return f"Бренд машины {self.brend} и модель {self.model}"


car = Car("Mers", "W210", 1920)

print(car.description())

"""
# 2 Задача
"""
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, salary) -> None:
        super().__init__(name, age)
        self.salary = salary

    def get_info(self):
        return f"Имя: {self.name}, возрост: {self.age}"

person = Employee("Nurbek", 28, 500000)
print(person.get_info())

"""

# 3 Задача

"""
class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return f"{self.name} Гав"


class Cat(Animal):
    def speak(self):
        return f"{self.name} Мяу"


dog = Dog("Reks")
print(dog.speak())
"""
