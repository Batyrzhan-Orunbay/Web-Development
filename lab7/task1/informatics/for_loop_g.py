# For Loop - Problem G: Sum of digits of a number
n = input().strip()
print(sum(int(d) for d in n if d.isdigit()))
