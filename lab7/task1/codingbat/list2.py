def count_evens(nums):
    """Return count of even numbers."""
    return sum(1 for n in nums if n % 2 == 0)


def big_diff(nums):
    """Return difference between max and min."""
    return max(nums) - min(nums)


def centered_average(nums):
    """Return average of nums after removing min and max."""
    nums = sorted(nums)
    return sum(nums[1:-1]) // (len(nums) - 2)


def sum13(nums):
    """Return sum, skipping 13 and the element after it."""
    total = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
        else:
            total += nums[i]
            i += 1
    return total


def sum67(nums):
    """Return sum, skipping numbers between 6 and 7 inclusive."""
    total = 0
    skip = False
    for n in nums:
        if n == 6:
            skip = True
        elif n == 7 and skip:
            skip = False
        elif not skip:
            total += n
    return total


def has22(nums):
    """Return True if 2 appears adjacent to another 2."""
    return any(nums[i] == 2 and nums[i + 1] == 2 for i in range(len(nums) - 1))
