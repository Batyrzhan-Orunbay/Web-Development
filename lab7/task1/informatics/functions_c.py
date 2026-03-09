# Functions - Problem C: Function to convert temperature Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit."""
    return celsius * 9 / 5 + 32


c = float(input())
print(f"{celsius_to_fahrenheit(c):.2f}")
