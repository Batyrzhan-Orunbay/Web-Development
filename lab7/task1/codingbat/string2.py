def double_char(s):
    """Return string with each char doubled."""
    return "".join(c * 2 for c in s)


def count_hi(s):
    """Count occurrences of 'hi' in string."""
    return s.count("hi")


def cat_dog(s):
    """Return True if 'cat' and 'dog' appear same number of times."""
    return s.count("cat") == s.count("dog")


def count_code(s):
    """Count 'code' patterns where any char can be between co_e."""
    count = 0
    for i in range(len(s) - 3):
        if s[i:i + 2] == "co" and s[i + 3] == "e":
            count += 1
    return count


def end_other(a, b):
    """Return True if one string ends with the other (case insensitive)."""
    a, b = a.lower(), b.lower()
    return a.endswith(b) or b.endswith(a)


def xyz_there(s):
    """Return True if 'xyz' appears, but not '.xyz'."""
    for i in range(len(s) - 2):
        if s[i:i + 3] == "xyz" and (i == 0 or s[i - 1] != "."):
            return True
    return False
