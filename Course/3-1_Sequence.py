def count(s, value):
    """Count the number of times that value offers
    in sequence s.
    >>> count([1, 2, 1, 2, 1], 1)
    3
    """
    total = 0
    for element in s:
        if element == value:
            total += 1
    return total

def sum_below(n):
    """
    >>> sum_below(5)
    10
    """
    total = 0
    for i in range(n):
        total += i
    return total

def cheer():
    """
    >>> cheer()
    Go Beers!
    Go Beers!
    Go Beers!
    """
    for _ in range(3):
        print("Go Beers!")

def division(n):
    """
    >>> division(1)
    [1]
    >>> division(4)
    [1, 2]
    >>> division(9)
    [1, 3]
    """
    return [1] + [x for x in range(2, n) if n % x == 0]

# Constructor and Selectors
def rational(n, d):
    """Construct a rational number x that represents n/d."""
    return [n, d]

def numer(x):
    """Return the numerator of rational number x."""
    return x[0]

def denom(x):
    """Return the denominator of rational number x."""
    return x[1]

# Rational arithmetic
def add_rational(x,y):
    """Add rational numbers x and y."""
    nx, dx = numer(x), denom(y)
    ny, dy = numer(y), denom(x)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    """Multiply rational numbers x and y."""
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def rationals_are_equal(x, y):
    """Return whether rational numbers x and y are equal."""
    return numer(x) * denom(y) == numer(y) * denom(x)

def print_rational(x):
    """Print rational x.
    >>> x, y = rational(1, 2), rational(3, 8)
    >>> print_rational(mul_rational(x, y))
    3 / 16
    """
    print(numer(x), "/", denom(x))
