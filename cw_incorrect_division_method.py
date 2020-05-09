"""Codewars: Incorrect division method
8 kyu

URL: https://www.codewars.com/kata/54d1c59aba326343c80000e7/train/python

This method, which is supposed to return the result of dividing its first 
argument by its second, isn't always returning correct values. Fix it.
"""


def divide_numbers(x,y):
    if x % y != 0:
        return x*1.0 / y*1.0
    else:
        return x // y


def divide_numbers1(x,y):
    return float(x) / float(y)


def main():
    # Output: 2
    x, y = 4, 2
    print(divide_numbers(x,y))

    # Output: 5
    x, y = 10, 2
    print(divide_numbers(x,y))

    # Output: 2.25
    x, y = 9, 4
    print(divide_numbers(x,y))

    # Output: 4.2
    x, y = 21, 5
    print(divide_numbers(x,y))

    # Output: 3
    x, y = 9, 3
    print(divide_numbers(x,y))

    # Output: 0.01
    x, y = 1, 100
    print(divide_numbers(x,y))

    # assert divide_numbers(4, 2)
    # assert divide_numbers(10, 2)
    # assert divide_numbers(9, 4)
    # assert divide_numbers(21, 5)
    # assert divide_numbers(9, 3)
    # assert divide_numbers(1, 100)


if __name__ == "__main__":
    main()

