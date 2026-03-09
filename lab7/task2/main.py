"""
main.py - Demonstrates usage of the Animal class hierarchy.

This script creates instances of Animal, Dog, and Cat classes,
stores them in a list, and demonstrates polymorphism.
"""

from models import Animal, Dog, Cat


def demonstrate_polymorphism(animals):
    """
    Demonstrate polymorphism by calling speak() and describe() on all animals.

    Args:
        animals (list): A list of Animal objects (or subclasses).
    """
    print("=" * 50)
    print("Polymorphism Demo: Each animal speaks differently")
    print("=" * 50)
    for animal in animals:
        print(f"\n{animal.name} says: {animal.speak()}")
        print(f"Description: {animal.describe()}")


def demonstrate_unique_methods(animals):
    """
    Demonstrate unique methods of each subclass.

    Args:
        animals (list): A list of Animal objects.
    """
    print("\n" + "=" * 50)
    print("Unique Methods Demo")
    print("=" * 50)
    for animal in animals:
        if isinstance(animal, Dog):
            print(f"\n{animal.fetch('ball')}")
        elif isinstance(animal, Cat):
            print(f"\n{animal.purr()}")


def main():
    """Main function to demonstrate the Animal class hierarchy."""
    generic_animal = Animal(name="Generic", age=5, species="Unknown")
    dog1 = Dog(name="Buddy", age=3, breed="Golden Retriever", is_trained=True)
    dog2 = Dog(name="Max", age=1, breed="Labrador", is_trained=False)
    cat1 = Cat(name="Whiskers", age=4, color="orange", is_indoor=True)
    cat2 = Cat(name="Shadow", age=2, color="black", is_indoor=False)

    animals = [generic_animal, dog1, dog2, cat1, cat2]

    print("=" * 50)
    print("All Animals (__str__ representation):")
    print("=" * 50)
    for animal in animals:
        print(animal)

    demonstrate_polymorphism(animals)

    demonstrate_unique_methods(animals)

    print("\n" + "=" * 50)
    print("Animals older than 2 years:")
    print("=" * 50)
    older_animals = [a for a in animals if a.age > 2]
    for animal in older_animals:
        print(f"  - {animal.name} ({animal.species}), age {animal.age}")


if __name__ == "__main__":
    main()
