# While Loop - Problem C: Reverse a number
n = abs(int(input()))
reversed_n = 0
while n > 0:
    reversed_n = reversed_n * 10 + n % 10
    n //= 10
print(reversed_n)
