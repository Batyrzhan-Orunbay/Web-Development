# For Loop - Problem M: Print Fibonacci sequence up to n terms
n = int(input())
a, b = 0, 1
for _ in range(n):
    print(a)
    a, b = b, a + b
