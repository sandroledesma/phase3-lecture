class Pet: # Parent class to Dog and cat and Bird
    def __init__(self, name, age, sound="hello"): 
        self.name = name 
        self.age = age
        self.sound = sound

    def say_hi(self):
        print(self.sound)

    def __repr__(self):
        return f'<Pet name: {self.name}, age: {self.age} >'

class Dog(Pet):
    def __init__(self, name, age, breed): 
        super().__init__(name, age, sound="bark") # calls the parent constructor
        self.breed = breed

    def say_hi(self):
        super().say_hi()
        print("dog wags tail")

    def __repr__(self):
        return f'<Dog name: {self.name}, age: {self.age} >'
    
class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age, sound="meow")

    def __repr__(self):
        return f'<Cat name: {self.name}, age: {self.age} >'