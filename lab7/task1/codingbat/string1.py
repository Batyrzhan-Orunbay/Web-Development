def hello_name(name):
    """Return 'Hello name!'"""
    return f"Hello {name}!"


def make_abba(a, b):
    """Return a+b+b+a."""
    return a + b + b + a


def make_tags(tag, word):
    """Wrap word in HTML tag."""
    return f"<{tag}>{word}</{tag}>"


def make_out_word(out, word):
    """Surround word with out characters split in half."""
    half = len(out) // 2
    return out[:half] + word + out[half:]


def extra_end(s):
    """Return last 2 chars of s, 3 times."""
    return s[-2:] * 3


def first_two(s):
    """Return first 2 characters of s."""
    return s[:2]


def first_half(s):
    """Return first half of even-length string."""
    return s[:len(s) // 2]


def without_end(s):
    """Return string without first and last chars."""
    return s[1:-1]


def combo_string(a, b):
    """Return shorter string + longer + shorter."""
    short, long = (a, b) if len(a) <= len(b) else (b, a)
    return short + long + short


def non_start(a, b):
    """Return a[1:] + b[1:]."""
    return a[1:] + b[1:]


def left2(s):
    """Rotate string 2 characters to the left."""
    return s[2:] + s[:2]
