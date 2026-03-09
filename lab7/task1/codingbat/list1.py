def first_last6(nums):
    """Return True if first or last element is 6."""
    return nums[0] == 6 or nums[-1] == 6


def same_first_last(nums):
    """Return True if first and last elements are equal."""
    return len(nums) >= 1 and nums[0] == nums[-1]


def make_pi():
    """Return first 3 elements of pi as list."""
    return [3, 1, 4]


def common_end(a, b):
    """Return True if lists share a common end element."""
    return a[0] == b[0] or a[-1] == b[-1]


def sum3(nums):
    """Return sum of first 3 elements."""
    return sum(nums[:3])


def rotate_left3(nums):
    """Rotate list left by 1."""
    return nums[1:] + nums[:1]


def reverse3(nums):
    """Reverse a 3-element list."""
    return nums[::-1]


def max_end3(nums):
    """Fill 3-element list with max of first/last."""
    m = max(nums[0], nums[2])
    return [m, m, m]


def sum2(nums):
    """Return sum of first 2 elements, or 0 if empty."""
    return sum(nums[:2])


def middle_way(a, b):
    """Return middle element of each 3-element list."""
    return [a[1], b[1]]


def make_ends(nums):
    """Return list of first and last elements."""
    return [nums[0], nums[-1]]


def has23(nums):
    """Return True if 2 or 3 appears in 2-element list."""
    return 2 in nums or 3 in nums
