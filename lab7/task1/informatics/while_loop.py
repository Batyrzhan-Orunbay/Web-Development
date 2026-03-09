# While Loop — Problems A–E

# Problem A: Count down from N to 1
n = int(input())
while n > 0:
    print(n)
    n -= 1

# Problem B: Sum until zero
# total = 0
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     total += n
# print(total)

# Problem C: Digits of a number
# n = int(input())
# digits = []
# while n > 0:
#     digits.append(n % 10)
#     n //= 10
# print(*reversed(digits))

# Problem D: GCD using Euclidean algorithm
# a, b = map(int, input().split())
# while b:
#     a, b = b, a % b
# print(a)

# Problem E: Collatz sequence
# n = int(input())
# while n != 1:
#     print(n)
#     if n % 2 == 0:
#         n //= 2
#     else:
#         n = 3 * n + 1
# print(1)
