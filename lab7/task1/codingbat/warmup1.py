def sleep_in(weekday, vacation):
    """Return True if we can sleep in (not weekday, or on vacation)."""
    return not weekday or vacation


def monkey_trouble(a_smile, b_smile):
    """Return True if both monkeys are smiling or neither is smiling."""
    return a_smile == b_smile


def sum_double(a, b):
    """Return sum of a+b; double it if they are equal."""
    total = a + b
    return total * 2 if a == b else total


def diff21(n):
    """Return absolute difference between n and 21; double if n > 21."""
    diff = abs(n - 21)
    return diff * 2 if n > 21 else diff


def parrot_trouble(talking, hour):
    """Return True if there's parrot trouble (talking outside 7-20 hours)."""
    return talking and (hour < 7 or hour > 20)


def makes10(a, b):
    """Return True if one is 10, or sum is 10."""
    return a == 10 or b == 10 or a + b == 10


def near_hundred(n):
    """Return True if within 10 of 100 or 200."""
    return abs(100 - n) <= 10 or abs(200 - n) <= 10


def pos_neg(a, b, negative):
    """Return True if one is negative and other is positive, or both negative if flag is set."""
    if negative:
        return a < 0 and b < 0
    return (a < 0 and b > 0) or (a > 0 and b < 0)


def not_string(s):
    """Add 'not ' in front unless already starts with 'not'."""
    if s.startswith("not"):
        return s
    return "not " + s


def missing_char(s, n):
    """Return string missing char at index n."""
    return s[:n] + s[n + 1:]


def front_back(s):
    """Swap first and last characters."""
    if len(s) <= 1:
        return s
    return s[-1] + s[1:-1] + s[0]


def front3(s):
    """Return 3 copies of first 3 characters."""
    front = s[:3]
    return front * 3
