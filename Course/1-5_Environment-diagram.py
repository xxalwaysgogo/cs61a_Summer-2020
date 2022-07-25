from operator import add

def apply_twice(f, x):
    """
    >>> apply_twice(square, 3)
    81
    """
    return f(f(x))

def square(x):
    return x * x

def repeat(f, x):
    while f(x) != x:
        x = f(x)
    return x

def g(y):
    """
    >>> repeat(g, 5)
    2
    """
    return (y + 5) // 3

def make_adder(n):
    """
    >>> adder_three = make_adder(3)
    >>> adder_three(4)
    7
    >>> make_adder(4)(1)
    5
    """
    def adder(k):
        return k + n
    return adder

def square(x):
    """
    >>> square(5)
    25
    """
    return x * x

def triple(x):
    """
    >>> triple(5)
    15
    """
    return 3 * x

def compose1(f, g):
    """
    >>> squiple = compose1(square, triple)
    >>> squiple(5)
    225
    >>> compose1(square, triple)(5)
    225
    >>> compose1(triple, square)(5)
    75
    >>> compose1(square, make_adder(2))(3)
    25
    """
    def h(x):
        return f(g(x))
    return h

def curry2(f):
    """
    >>> add(2,3)
    5
    >>> curry2(add)(2)(3)
    5
    >>> curry2 = lambda f: lambda x: lambda y: f(x, y)
    >>> m = curry2(add)
    >>> m(2)(3)
    5
    """
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def remove(n, digit):
    """Return all digits of non-negative N that arre not DIGIT,
        for some non-negative DIGIT less than 10.
    >>> remove(231, 3)
    21
    >>> remove(243132, 2)
    4313
    """
    kept, digits = 0, 0
    while n > 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept += last * 10 ** digits
            digits += 1
    return kept