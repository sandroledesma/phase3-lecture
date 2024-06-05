"""
Write a class that represents a dog. We should be able to:
- Access the dog's name, breed, and age
- Make the dog bark
- Print the dog as a string
"""

class Dog:
    def __init__(self, name, age, breed): 
    # in order to create an optional object, add 'placeholders' on an object 
    # def __init__(self, name, age, breed='unknown):
        self.name = name 
        self.age = age
        self.breed = breed

    def __repr__(self):
        return f'<Dog name: {self.name}, age: {self.age}, breed: {self.breed}>'
    
d1 = Dog('Lucy', 6, "Boxer Mix")
print(d1)