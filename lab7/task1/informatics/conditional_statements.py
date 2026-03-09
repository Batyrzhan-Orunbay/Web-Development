# Conditional Statements — Problems A–E

# Problem A: Positive, negative, or zero
def problem_a():
    n = int(input())
    if n > 0:
        print("positive")
    elif n < 0:
        print("negative")
    else:
        print("zero")


# Problem B: Max of two numbers
def problem_b():
    a, b = map(int, input().split())
    print(a if a > b else b)


# Problem C: Max of three numbers
def problem_c():
    a, b, c = map(int, input().split())
    print(max(a, b, c))


# Problem D: Even or odd
def problem_d():
    n = int(input())
    print("even" if n % 2 == 0 else "odd")


# Problem E: Leap year
def problem_e():
    year = int(input())
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("YES")
    else:
        print("NO")
