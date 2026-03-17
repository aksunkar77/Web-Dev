# main.py
# models.py-с классуудыг импортлоно
from models import Animal, Dog, Cat

# 1. Үндсэн class-ийн объект үүсгэх
animal = Animal("GenericAnimal", 5, "Unknown")

# 2. Dog object үүсгэх
dog = Dog("Buddy", 3, "Golden Retriever")

# 3. Cat object үүсгэх
cat = Cat("Misty", 2, "Black")

# 4. Бүх объектуудыг list-д хадгалах
animals = [animal, dog, cat]

# 5. Iterate хийж object-уудын мэдээллийг хэвлэх
for a in animals:
    print(a)          # __str__ ашиглана
    print(a.speak())  # Polymorphism: speak() нь object-ийн төрөлд шалтгаалан өөрөөр ажиллана
    print()