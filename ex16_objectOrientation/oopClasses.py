class Car:

    def __init__(self, colour, miles):
        self._colour = colour
        self._miles = miles

    def __str__(self):
        return f'The {self._colour} car has {self._miles} miles.'


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class GoldenRetriever(Dog):

    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self, sound="Bark"):
        return super().speak(sound)
