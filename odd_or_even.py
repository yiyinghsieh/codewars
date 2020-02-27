"""Odd or Even?
7 kyu

URL: https://www.codewars.com/kata/5949481f86420f59480000e7/train/python

Task:
Given a list of numbers, determine whether the sum of its elements is odd 
or even.
Give your answer as a string matching "odd" or "even".
If the input array is empty consider it as: [0] (array with a zero).

Example:
odd_or_even([0])          ==  "even"
odd_or_even([0, 1, 4])    ==  "odd"
odd_or_even([0, -1, -5])  ==  "even"
Have fun!
"""


def odd_or_even(arr):
    arr_sum = 0
    for d in arr:
        arr_sum += d
    if arr_sum % 2 == 0 or arr_sum == 0:
        return 'even'
    else:
        return 'odd'


def odd_or_even(arr):
    arr_sum = sum(d for d in arr)
    if arr_sum % 2 == 0 or arr_sum == 0:
        return 'even'
    else:
        return 'odd'


def odd_or_even(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'


def main():
    assert odd_or_even([0]) == "even"
    assert odd_or_even([0, 1, 2]) == "odd"
    assert odd_or_even([0, 1, 3]) == "even"
    assert odd_or_even([1023, 1, 2]) == "even"


if __name__ == '__main__':
    main()

