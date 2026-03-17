
class Animal:
    def __init__(self, name, age, species):
        # attributes - объектын шинж чанарууд
        self.name = name
        self.age = age
        self.species = species

    def speak(self):
        # Base class-ийн default method
        return "Some sound"

    def info(self):
        # Мэдээлэл харуулах method
        return f"{self.name} is a {self.age}-year-old {self.species}"

    def __str__(self):
        # print(object) хийхэд гарах текст
        return self.info()


# 2. Child class - Dog
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Dog")  # Base class-ийн constructor-ыг ашиглана
        self.breed = breed  # Dog-д нэмэлт attribute

    def speak(self):
        # Dog-д зориулсан өөрийн дууны method (override)
        return "Woof!"

    def info(self):
        # Dog-д зориулсан мэдээлэл override
        return f"{self.name} is a {self.age}-year-old {self.breed} dog"


# 3. Child class - Cat
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, "Cat")
        self.color = color  # Cat-д зориулсан attribute

    def speak(self):
        return "Meow!"  # Cat-ийн дуу

    def info(self):
        return f"{self.name} is a {self.age}-year-old {self.color} cat"