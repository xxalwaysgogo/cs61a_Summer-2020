def fib(n):
    """
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(5)
    5
    >>> fib(30)
    832040
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


def path(m, n):
    """
    >>> path(2, 2)
    2
    >>> path(5, 7)
    210
    """
    if m == 1 or n == 1:
        return 1
    return path(m-1, n) + path(m, n-1)

def knap(n, k):
    """
    >>> knap(689, 16)
    False
    """
    if n == 0:
        return k == 0
    with_last = knap(n // 10, k - n % 10)
    without_last = knap(n // 10, k)
    return with_last or without_last

def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n,m-1)
    return with_m + without_m