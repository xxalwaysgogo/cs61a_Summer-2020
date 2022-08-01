def split(n):
    """
    >>> after, last = split(2013)
    >>> after
    201
    >>> last
    3
    """
    return n // 10, n % 10

def sum_digits(n):
    """Return the sum of the digits of positive integer n.
    >>> sum_digits(2013)
    6
    >>> sum_digits(45674)
    26
    """
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

def luhn_sum(n):
    """
    >>> luhn_sum(6060456597624277)
    70
    """
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

def sum_digits_iter(n):
    digit_sum = 0
    while n > 0:
        n, last = split(n)
        digit_sum += last
    return digit_sum

def cascade(n):
    """
    >>> cascade(5)
    5
    >>> cascade(12345)
    12345
    1234
    123
    12
    1
    12
    123
    1234
    12345
    """
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)
