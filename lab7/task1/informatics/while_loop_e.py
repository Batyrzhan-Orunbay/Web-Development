# While Loop - Problem E: GCD using Euclidean algorithm
a = int(input())
b = int(input())
while b:
    a, b = b, a % b
print(a)
