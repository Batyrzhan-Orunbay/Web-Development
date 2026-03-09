"""
models.py - Animal class hierarchy demonstrating OOP concepts.

This module defines a base Animal class and child classes
Dog and Cat with inheritance and method overriding.
"""


class Animal:
    """
    Base class representing a generic animal.

    Attributes:
        name (str): The animal's name.
        age (int): The animal's age in years.
        species (str): The species of the animal.
    """

    def __init__(self, name, age, species):
        """
        Initialize an Animal instance.

        Args:
            name (str): The animal's name.
            age (int): The animal's age in years.
            species (str): The species of the animal.
        """
        self.name = name
        self.age = age
        self.species = species

    def speak(self):
        """Return a generic sound for the animal."""
        return "..."

    def describe(self):
        """Return a description of the animal."""
        return f"{self.name} is a {self.age}-year-old {self.species}."

    def __str__(self):
        """Return string representation of the animal."""
        return f"Animal(name={self.name}, age={self.age}, species={self.species})"


class Dog(Animal):
    """
    Child class representing a dog.

    Inherits from Animal and adds breed-specific attributes and methods.

    Attributes:
        breed (str): The dog's breed.
        is_trained (bool): Whether the dog is trained.
    """

    def __init__(self, name, age, breed, is_trained=False):
        """
        Initialize a Dog instance.

        Args:
            name (str): The dog's name.
            age (int): The dog's age in years.
            breed (str): The dog's breed.
            is_trained (bool): Whether the dog is trained. Defaults to False.
        """
        super().__init__(name, age, species="Dog")
        self.breed = breed
        self.is_trained = is_trained

    def speak(self):
        """Return the dog's bark sound."""
        return "Woof! Woof!"

    def fetch(self, item):
        """
        Simulate the dog fetching an item.

        Args:
            item (str): The item to fetch.

        Returns:
            str: A message describing the fetch action.
        """
        return f"{self.name} fetches the {item}!"

    def describe(self):
        """Return a detailed description of the dog."""
        trained_status = "trained" if self.is_trained else "not trained"
        return (
            f"{self.name} is a {self.age}-year-old {self.breed} dog "
            f"and is {trained_status}."
        )

    def __str__(self):
        """Return string representation of the dog."""
        return (
            f"Dog(name={self.name}, age={self.age}, "
            f"breed={self.breed}, trained={self.is_trained})"
        )


class Cat(Animal):
    """
    Child class representing a cat.

    Inherits from Animal and adds indoor/outdoor and color attributes.

    Attributes:
        color (str): The cat's fur color.
        is_indoor (bool): Whether the cat is an indoor cat.
    """

    def __init__(self, name, age, color, is_indoor=True):
        """
        Initialize a Cat instance.

        Args:
            name (str): The cat's name.
            age (int): The cat's age in years.
            color (str): The cat's fur color.
            is_indoor (bool): Whether the cat is indoors. Defaults to True.
        """
        super().__init__(name, age, species="Cat")
        self.color = color
        self.is_indoor = is_indoor

    def speak(self):
        """Return the cat's meow sound."""
        return "Meow!"

    def purr(self):
        """
        Simulate the cat purring.

        Returns:
            str: A purring message.
        """
        return f"{self.name} purrs contentedly... Purrr~"

    def describe(self):
        """Return a detailed description of the cat."""
        location = "indoor" if self.is_indoor else "outdoor"
        return (
            f"{self.name} is a {self.age}-year-old {self.color} {location} cat."
        )

    def __str__(self):
        """Return string representation of the cat."""
        return (
            f"Cat(name={self.name}, age={self.age}, "
            f"color={self.color}, indoor={self.is_indoor})"
        )
