"""
Write a class that represents a dog. We should be able to:
- Access the dog's name, breed, and age
- Make the dog bark
- Print the dog as a string
"""

class Dog:
    all = [] # class attribute (youre building dog.all)
    genus = "canine"

    @classmethod
    def print_all_dogs(cls):
        print(Dog)
        print(cls) # reference to the class will be the same as print(Dog)
        for dog in Dog.all:
            print(dog) 

    def __init__(self, name, age, breed="unknown", is_good=True): 
    # in order to create an optional object, add 'placeholders' on an object 
    # def __init__(self, name, age, breed='unknown):
        self.name = name 
        self.age = age
        self.breed = breed
        self.is_good = is_good
        Dog.all.append(self)

    def __repr__(self):
        return f'<Dog {Dog.genus} name: {self.name}, age: {self.age}, breed: {self.breed}, {self.is_good}>'
    
d1 = Dog('Lucy', 6, "Boxer Mix")


print(d1)