# Functions - Problem B: Recursive function for Fibonacci number
def fibonacci(n):
    """Return the nth Fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input())
print(fibonacci(n))
