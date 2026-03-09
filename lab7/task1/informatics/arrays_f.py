# Arrays - Problem F: Remove duplicates from array
n = int(input())
nums = list(map(int, input().split()))
unique = list(dict.fromkeys(nums))
print(*unique)
