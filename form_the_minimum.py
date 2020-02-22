"""Form The Minimum
7 kyu

URL: https://www.codewars.com/kata/5ac6932b2f317b96980000ca/train/python

Task
Given a list of digits, return the smallest number that could be formed 
from these digits, using the digits only once (ignore duplicates).

Notes:
Only positive integers will be passed to the function (> 0 ), 
no negatives or zeros.

Examples:
minValue ({1, 3, 1})  ==> return (13)
Explanation:
(13) is the minimum number could be formed from {1, 3, 1} , Without 
duplications
"""


def min_value(digits):
    """Apply string join approach."""
    sorted_digits_ls = sorted(set(digits))
    lst = []
    for d in sorted_digits_ls:
        lst.append(str(d))
    return int(''.join(lst))


def min_value2(digits):
    """Apply 10 to the powers approach."""
    sorted_digits_ls = sorted(set(digits))
    value = 0
    for p, d in enumerate(reversed(sorted_digits_ls)):
        # Why reverse? [1, 4, 8] => [8, 4, 1] w/ power 0, 1, 2.
        value += d * (10 ** p)
    return value


def main():
    # Output: 13
    digits = [1, 3, 1]
    print(min_value(digits))
    print(min_value2(digits))

    # Output: 457
    digits = [4, 7, 5, 7]
    print(min_value(digits))
    print(min_value2(digits))

    # Output: 148
    digits = [4, 8, 1, 4]
    print(min_value(digits))
    print(min_value2(digits))


if __name__ == '__main__':
    main()


