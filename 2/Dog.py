# Dog нь Animal-ийн child class
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Dog")  # Parent-ийн __init__-г дуудаж нэр, нас, төрөл өгнө
        self.breed = breed  # Dog-д зориулсан өөр attribute нэмнэ

    def speak(self):
        # Parent class-ийн speak()-г override хийж, Dog-ийн дууг гаргана
        return "Woof!"

    def info(self):
        # Parent class-ийн info()-г override хийж, dog-т зориулсан мэдээллийг харуулна
        return f"{self.name} is a {self.age}-year-old {self.breed} dog"