"""Codewars: Count the Monkeys!
8 kyu

URL: https://www.codewars.com/kata/56f69d9f9400f508fb000ba7/train/python

You take your son to the forest to see the monkeys. You know that there are a 
certain number there (n), but your son is too young to just appreciate the full 
number, he has to start counting them from 1.

As a good parent, you will sit and count with him. Given the number (n), 
populate an array with all numbers up to and including that number, 
but excluding zero.

For example:

monkeyCount(10) # --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
monkeyCount(1) # --> [1]
"""


from __future__ import division
from __future__ import print_function

def monkey_count(n):
    return list(range(1, n + 1))


def main():
    # Output: [1, 2, 3, 4, 5]
    n = 5
    print(monkey_count(n))
    # Output: [1, 2, 3]
    n = 3
    print(monkey_count(n))
    # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = 9
    print(monkey_count(n))
    # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 10
    print(monkey_count(n))
    # Output:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    n = 20
    print(monkey_count(n))


if __name__ == '__main__':
    main()


