# Cat нь Animal-ийн child class
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, "Cat")  # Parent-ийн constructor дуудна
        self.color = color  # Cat-д зориулсан шинж чанар

    def speak(self):
        # Cat-ийн дуу
        return "Meow!"

    def info(self):
        # Cat-д зориулсан мэдээлэл
        return f"{self.name} is a {self.age}-year-old {self.color} cat"