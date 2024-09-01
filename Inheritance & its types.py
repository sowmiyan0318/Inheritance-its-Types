#Single Inheritance
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

# Child class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} is barking.")

my_dog = Dog("Rex", "Golden Retriever")
my_dog.eat()# Output: Rex is eating.
my_dog.bark() # Output: Rex the Golden Retriever is barking.


#Multiple Inheritance

# Parent class 1
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

# Parent class 2
class Mammal:
    def __init__(self, hair_color):
        self.hair_color = hair_color

    def feed_young(self):
        print(f"The {self.hair_color} mammal is feeding its young.")

# Child class
class Dog(Animal, Mammal):
    def __init__(self, name, breed, hair_color):
        Animal.__init__(self, name)
        Mammal.__init__(self, hair_color)
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} is barking.")

my_dog = Dog("Rex", "Golden Retriever", "Brown")
my_dog.eat()  # Output: Rex is eating.
my_dog.feed_young()  # Output: The Brown mammal is feeding its young.
my_dog.bark()  # Output: Rex the Golden Retriever is barking.

# Multilevel Inheritance

# Grandparent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

# Parent class
class Mammal(Animal):
    def __init__(self, name, hair_color):
        super().__init__(name)
        self.hair_color = hair_color

    def feed_young(self):
        print(f"The {self.hair_color} mammal is feeding its young.")

# Child class
class Dog(Mammal):
    def __init__(self, name, breed, hair_color):
        super().__init__(name, hair_color)
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} is barking.")

my_dog = Dog("Rex", "Golden Retriever", "Brown")
my_dog.eat()  # Output: Rex is eating.
my_dog.feed_young()  # Output: The Brown mammal is feeding its young.
my_dog.bark()  # Output: Rex the Golden Retriever is barking.

#Hierarchical Inheritance

# Parent class
class Animal:
    def __init__(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

# Child class 1
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        if not breed:
            raise ValueError("Breed cannot be empty")
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} is barking.")

    def play_fetch(self):
        print(f"{self.name} is playing fetch!")

# Child class 2
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        if not color:
            raise ValueError("Color cannot be empty")
        self.color = color

    def meow(self):
        print(f"{self.name} the {self.color} cat is meowing.")

    def scratch_post(self):
        print(f"{self.name} is scratching the post!")

my_dog = Dog("Rex", "Golden Retriever")
my_dog.eat()  # Output: Rex is eating.
my_dog.bark()  # Output: Rex the Golden Retriever is barking.
my_dog.play_fetch()  # Output: Rex is playing fetch!

my_cat = Cat("Whiskers", "Grey")
my_cat.eat()  # Output: Whiskers is eating.
my_cat.meow()  # Output: Whiskers the Grey cat is meowing.
my_cat.scratch_post()  # Output: Whiskers is scratching the post!
