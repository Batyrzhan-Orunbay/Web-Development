# For Loop - Problem J: Power of a number (a^b)
a = int(input())
b = int(input())
result = 1
for _ in range(b):
    result *= a
print(result)
