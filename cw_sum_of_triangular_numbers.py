"""Codewars: Sum of Triangular Numbers
7 kyu

URL: https://www.codewars.com/kata/580878d5d27b84b64c000b51/train/python
Your task is to return the sum of Triangular Numbers up-to-and-including 
the nth Triangular Number.

Triangular Number: "any of the series of numbers (1, 3, 6, 10, 15, etc.) 
obtained by continued summation of the natural numbers 1, 2, 3, 4, 5, etc."

[01]
02 [03]
04 05 [06]
07 08 09 [10]
11 12 13 14 [15]
16 17 18 19 20 [21]
e.g. If 4 is given: 1 + 3 + 6 + 10 = 20.

Triangular Numbers cannot be negative so return 0 if a negative number is 
given.
"""


def sum_triangular_numbers(n):
    sum_d, sum_n = 0, 0
    if n < 1:
        return 0
    for d in range(n + 1):
        sum_d += d
        sum_n += sum_d
    return sum_n
        

def main():
    # Output: 56
    # n = 6
    # print(sum_triangular_numbers(n))

    assert sum_triangular_numbers(6) == 56
    assert sum_triangular_numbers(34) == 7140
    assert sum_triangular_numbers(-291) == 0
    assert sum_triangular_numbers(943) == 140205240
    assert sum_triangular_numbers(-971) == 0


if __name__ == '__main__':
    main()

    