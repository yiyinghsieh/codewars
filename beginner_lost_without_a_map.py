"""Codewars: Beginner - Lost Without a Map
8 kyu

URL: https://www.codewars.com/kata/beginner-lost-without-a-map/train/python

Given an array of integers, return a new array with each value doubled.

For example:
[1, 2, 3] --> [2, 4, 6]

For the beginner, try to use the map method - 
it comes in very handy quite a lot so is a good one to know.
"""


from __future__ import division
from __future__ import print_function


def maps(a):
    lst = []
    for num in a:
        lst.append(num * 2)
    return lst


def maps(a):
    for i in range(len(a)):
        a[i] *= 2
    return a

    
def main():
    # Output: [2, 4, 6]
    a = [1, 2, 3]
    print(maps(a))

    # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(maps(a))

    # Output: []
    a = []
    print(maps(a))


if __name__ == '__main__':
    main()


