def string_times(s, n):
    """Return n copies of string s."""
    return s * n


def front_times(s, n):
    """Return first 3 chars of s repeated n times."""
    return s[:3] * n


def string_bits(s):
    """Return every other character starting from index 0."""
    return s[::2]


def string_splosion(s):
    """Return exploded string: 'Code' -> 'CCoCodCode'."""
    return "".join(s[:i + 1] for i in range(len(s)))


def last2(s):
    """Count occurrences of last 2 chars in the string (excluding the final occurrence)."""
    if len(s) < 2:
        return 0
    last = s[-2:]
    count = 0
    for i in range(len(s) - 2):
        if s[i:i + 2] == last:
            count += 1
    return count


def array_count9(nums):
    """Return count of 9s in the list."""
    return nums.count(9)


def array_front9(nums):
    """Return True if 9 appears in first 4 elements."""
    return 9 in nums[:4]


def array123(nums):
    """Return True if 1, 2, 3 appear consecutively."""
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False


def string_match(a, b):
    """Count positions where 2-char substrings match."""
    count = 0
    for i in range(min(len(a), len(b)) - 1):
        if a[i:i + 2] == b[i:i + 2]:
            count += 1
    return count
