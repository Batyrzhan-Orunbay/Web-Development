# For Loop - Problem L: Find sum of odd numbers from 1 to n
n = int(input())
total = 0
for i in range(1, n + 1, 2):
    total += i
print(total)
