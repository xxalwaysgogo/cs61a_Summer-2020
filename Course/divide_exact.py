'''Our first Python source file.'''

from operator import floordiv, mod

def divide_exact(n, d):
    """Return the quorient and remainder of dividing N by D.
    >>> q, r = divide_exact(2013, 10)
    >>> q
    201
    >>> r
    3
    """
    return floordiv(n, d), mod(n, d)

def absolute_value(x):
    """Return the absolute value of x.
    >>> absolute_value(3)
    3
    >>> absolute_value(0)
    0
    >>> absolute_value(-3)
    3
    """
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x

def fib(n):
    """
    Compute the nth Fibonacci number.
    >>> fib(1)
    1
    >>> fib(4)
    3
    """
    pred, curr = 1, 0   # 0th and 1st Fibonacci numbers
    k = 0               # curr is the kth Fibonacci number
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr

def end(n, d):
    """
    Print the final digits of N in reverse order until D is found.
    >>> end(34567, 5)
    7
    6
    5
    """
    while n > 0:
        last, n = n % 10, n // 10
        print(last)
        if d == last:
            return None

def search(f):
    """
    >>> search(is_three)
    3
    """
    x = 0
    while True:
        if f(x):
            return x
        x += 1
def is_three(x):
    return x == 3

def square(x):
    return x * x

def positive(x):
    """
    >>> positive(2)
    0
    >>> positive(5)
    0
    >>> positive(10)
    0
    >>> positive(11)
    21
    """
    return max(0, square(x) - 100)

def inverse(f):
    """
    Return g(y) such that g(f(x)) -> x.
    >>> sqrt = inverse(square)
    >>> sqrt(256)
    16
    """
    return lambda y: search(lambda x: f(x) == y)

def if_(c, t, f):
    if c:
        return t
    else:
        return f

from math import sqrt

def real_sqrt(x):
    """
    The real part of the square root of X.
    >>> real_sqrt(4)
    2.0
    >>> real_sqrt(-4)
    0.0
    """
    if x > 0:
        return sqrt(x)
    else:
        return 0.0

def has_big_sqrt(x):
    """
    >>> has_big_sqrt(1)
    False
    >>> has_big_sqrt(1000)
    True
    >>> has_big_sqrt(-1000)
    False
    """
    return x > 0 and sqrt(x) > 10

def reasonalbe(n):
    """
    >>> reasonalbe(0)
    True
    >>> reasonalbe(10)
    True
    >>> reasonalbe(10 ** 10000)
    False
    """
    return n == 0 or 1 / n != 0

