"""Codewars: Find numbers which are divisible by given number
8 kyu

URL: https://www.codewars.com/kata/55edaba99da3a9c84000003b/train/python

Complete the function which takes two arguments and returns all numbers which 
are divisible by the given divisor. First argument is an array of numbers and 
the second is the divisor.

Example
divisible_by([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]
"""


def divisible_by(numbers, divisor):
    lst = []
    for num in numbers:
        if num % divisor == 0:
            lst.append(num)
    return lst


def divisible_by1(numbers, divisor):
    return [x for x in numbers if x%divisor == 0]


def main():
    # numbers, divisor = [1,3,5], 2
    # print(divisible_by(numbers, divisor))

    assert divisible_by([1,2,3,4,5,6], 2) == [2,4,6]
    assert divisible_by([1,2,3,4,5,6], 3)== [3,6]
    assert divisible_by([0,1,2,3,4,5,6], 4) == [0,4]
    assert divisible_by([0], 4) == [0]
    assert divisible_by([1,3,5], 2) == []


if __name__ == '__main__':
    main()

