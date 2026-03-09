# For Loop — Problems A–M

# Problem A: Print numbers from 1 to N
def problem_a():
    n = int(input())
    for i in range(1, n + 1):
        print(i)


# Problem B: Sum of numbers from 1 to N
def problem_b():
    n = int(input())
    print(sum(range(1, n + 1)))


# Problem C: Factorial
def problem_c():
    n = int(input())
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(result)


# Problem D: Sum of N numbers from input
def problem_d():
    n = int(input())
    total = 0
    for _ in range(n):
        total += int(input())
    print(total)


# Problem E: Count of even numbers
def problem_e():
    n = int(input())
    count = 0
    for _ in range(n):
        x = int(input())
        if x % 2 == 0:
            count += 1
    print(count)


# Problem F: Maximum of N numbers
def problem_f():
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    print(max(nums))


# Problem G: Reverse a sequence
def problem_g():
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    for x in reversed(nums):
        print(x)


# Problem H: Multiplication table
def problem_h():
    n = int(input())
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")


# Problem I: Sum of digits
def problem_i():
    n = input().strip()
    print(sum(int(d) for d in n))


# Problem J: Count digits
def problem_j():
    n = input().strip()
    print(len(n))


# Problem K: Stars pattern
def problem_k():
    n = int(input())
    for i in range(1, n + 1):
        print("*" * i)


# Problem L: Fibonacci sequence up to N terms
def problem_l():
    n = int(input())
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b


# Problem M: Prime check
def problem_m():
    n = int(input())
    if n < 2:
        print("NO")
        return
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("NO")
            return
    print("YES")
