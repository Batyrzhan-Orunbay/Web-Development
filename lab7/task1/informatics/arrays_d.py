# Arrays - Problem D: Count elements greater than average
n = int(input())
nums = list(map(int, input().split()))
avg = sum(nums) / n
print(sum(1 for x in nums if x > avg))
