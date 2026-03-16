# Object-уудыг list-д хадгалах
animals = [
    Dog("Buddy", 3, "Golden Retriever"),
    Cat("Misty", 2, "Black")
]

# Iterate хийж polymorphism-г харуулах
for a in animals:
    print(a.info())   # info() нь object-ийн төрөлд шалтгаалан өөрөөр ажиллана
    print(a.speak())  # speak() нь object-ийн төрөлд шалтгаалан өөрөөр ажиллана
    print()