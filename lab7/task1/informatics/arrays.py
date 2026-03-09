# Arrays (Lists) — Problems A–G

# Problem A: Read and print a list
n = int(input())
arr = list(map(int, input().split()))
print(*arr)

# Problem B: Reverse a list
# n = int(input())
# arr = list(map(int, input().split()))
# print(*arr[::-1])

# Problem C: Sum of list elements
# n = int(input())
# arr = list(map(int, input().split()))
# print(sum(arr))

# Problem D: Max and Min of list
# n = int(input())
# arr = list(map(int, input().split()))
# print(max(arr), min(arr))

# Problem E: Count even and odd numbers
# n = int(input())
# arr = list(map(int, input().split()))
# even = sum(1 for x in arr if x % 2 == 0)
# odd = n - even
# print(even, odd)

# Problem F: Sort a list
# n = int(input())
# arr = list(map(int, input().split()))
# print(*sorted(arr))

# Problem G: Remove duplicates
# n = int(input())
# arr = list(map(int, input().split()))
# seen = []
# for x in arr:
#     if x not in seen:
#         seen.append(x)
# print(*seen)
