def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    x, y = 1, 1
    for i in range(1, n + 1):
        x = i * x
    for i in range(1, n - k + 1):
        y = i * y
    return x // y


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    sum = 0
    while y > 0:
        last = y % 10
        y = y // 10
        sum += last
    return sum


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    if n // 10 == 0:
        return False
    while n:
        last = n % 10
        n //= 10
        if last == 8 == (n % 10):
            return True
    return False


def xk(c, d):
    """
    >>> xk(10, 10)
    23
    >>> xk(10, 6)
    23
    >>> xk(4, 6)
    6
    >>> xk(0, 0)
    25
     """
    if c == 4:
        return 6
    elif d >= 4:
        return 6 + 7 + c
    else:
        return 25

def how_big(x):
    """
    >>> how_big(7)
    'big'
    >>> how_big(12)
    huge
    >>> how_big(1)
    small
    >>> how_big(-1)
    nothing
    """
    if x > 10:
        print('huge')
    elif x > 5:
        return 'big'
    elif x > 0:
        print('small')
    else:
        print("nothing")

def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    "*** YOUR CODE HERE ***"
    if temp > 50:
        return raining
    else:
        return not raining


def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result is None  # No return value
    True
    """
    "*** YOUR CODE HERE ***"
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 != 0:
            print('fizz')
        elif i % 3 != 0 and i % 5 == 0:
            print('buzz')
        elif i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        else:
            print(i)




def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    uni, last = [], 0
    while n > 0:
        last, n = n % 10, n // 10
        if last == 0:
            uni.append(last)
        elif last == 1:
            uni.append(last)
        elif last == 2:
            uni = uni
        else:
            for i in range(2, last):
                if last % i != 0:
                    uni.append(last)
    uni = list(set(uni))
    return len(uni)

def has_digit(n, k):
    """Returns whether K is a digit in N.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    "*** YOUR CODE HERE ***"
    last = 0
    while n > 0:
        last, n = n % 10, n // 10
        if last == k:
            return True
    return False
