# Arrays - Problem G: Rotate array to the right by k positions
n = int(input())
nums = list(map(int, input().split()))
k = int(input()) % n
rotated = nums[-k:] + nums[:-k]
print(*rotated)
