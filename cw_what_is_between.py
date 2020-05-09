"""Codewars: What is between?
8 kyu

URL: https://www.codewars.com/kata/what-is-between/train/python

Complete the function that takes two integers (a, b, where a < b) 
and return an array of all integers between the input parameters, 
including them.

For example:
a = 1
b = 4
--> [1, 2, 3, 4]
"""


from __future__ import division
from __future__ import print_function


def between(a,b):
    lst = []
    while True:
        lst.append(a)
        if a != b:
            a += 1
        else:
            break

    return lst


def between2(a,b):
    lst = []
    while a <= b:
        lst.append(a)
        a += 1

    return lst


def between3(a,b):
    return list(range(a, b + 1))


def main():
    # Output: [1, 2, 3, 4]
    a, b = 1, 4
    print(between(a,b))

    # Output: [-2, -1, 0, 1, 2]
    a, b = -2, 2
    print(between(a,b))
        

if __name__ == '__main__':
    main()

