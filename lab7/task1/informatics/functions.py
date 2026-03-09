# Functions — Problems A–C

# Problem A: Function to check even/odd
def is_even(n):
    """Return True if n is even, False otherwise."""
    return n % 2 == 0


n = int(input())
print("Even" if is_even(n) else "Odd")


# Problem B: Function to compute factorial
def factorial(n):
    """Return the factorial of n."""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# n = int(input())
# print(factorial(n))


# Problem C: Function to check prime
def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# n = int(input())
# print("Prime" if is_prime(n) else "Not Prime")
