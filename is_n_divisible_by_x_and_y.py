"""Codewars: Is n divisible by x and y?
8 kyu

URL: https://www.codewars.com/kata/is-n-divisible-by-x-and-y/train/python

Create a function isDivisible(n, x, y) that checks if a number n is divisible 
by two numbers x AND y. All inputs are positive, non-zero digits.
Example:
is_divisible(3,1,3)--> True because 3 is divisible by 1 and 3
is_divisible(12,2,6)--> True because 12 is divisible by 2 and 6
is_divisible(100,5,3)--> False because 100 is not divisible by 3
is_divisible(12,7,5)--> False because 12 is neither divisible by 7 nor 5
"""

from __future__ import division
from __future__ import print_function


def is_divisible_remainder(n, x, y):
    divide1 = n / x
    divide2 = n / y
    if divide1 - int(divide1) != 0 or divide2 - int(divide2) != 0: 
        return False
    else:
        return True


def is_divisible_mod(n, x, y):
    modx = n % x
    mody = n % y
    if modx > 0 or mody > 0: 
        return False
    else:
        return True


def is_divisible_mod_1line(n, x, y):
    return (n % x == 0) and (n % y == 0)


def main():
    import time
    
    start_time = time.time()
    assert is_divisible_remainder(3, 3, 4) == False
    assert is_divisible_remainder(12, 3, 4) == True
    assert is_divisible_remainder(8, 3, 4) == False
    assert is_divisible_remainder(48, 3, 4) == True
    print('Time by remainder: {}'.format(time.time() - start_time))

    start_time = time.time()
    assert is_divisible_mod(3, 3, 4) == False
    assert is_divisible_mod(12, 3, 4) == True
    assert is_divisible_mod(8, 3, 4) == False
    assert is_divisible_mod(48, 3, 4) == True
    print('Time by mod: {}'.format(time.time() - start_time))

    start_time = time.time()
    assert is_divisible_mod_1line(3, 3, 4) == False
    assert is_divisible_mod_1line(12, 3, 4) == True
    assert is_divisible_mod_1line(8, 3, 4) == False
    assert is_divisible_mod_1line(48, 3, 4) == True
    print('Time by mod 1 line: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()

