"""Codewars: Persistent Bugger
6 kyu

URL: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

Write a function, persistence, that takes in a positive parameter num 
and returns its multiplicative persistence, which is the number of 
times you must multiply the digits in num until you reach a single 
digit.

For example:

persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit

persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

persistence(4) # returns 0, because 4 is already a one-dig
"""


def persistence1(n):
    multi_num = 1
    count = 1
    len_n = len(str(n))  # length, size
    
    if len_n < 2:
        return count - 1
    elif len_n >= 2:
        for len_num in range(len_n):
            multi_num = multi_num * int(str(n)[len_num])

    while len(str(multi_num)) >= 2:
        new_multi_num = multi_num
        multi_num = 1
        count += 1
        for len_num in range(len(str(new_multi_num))):
            multi_num = multi_num * int(str(new_multi_num)[len_num])
    return count


def _multiply(n_str):
    # Helper of persistence2(): Compute multiplication of n.
    multiply = 1
    for c in n_str:
        multiply *= int(c)
    return multiply


def persistence2(n):
    n_str = str(n)
    length = len(n_str)

    # Edge case for n's lenght is 1.
    if length == 1:
        return 0

    counter = 0
    while length >= 2:
        # Multiply n and increment counter.
        n_persist = _multiply(n_str)
        counter += 1

        # Update n and its length.
        n_str = str(n_persist)
        length = len(n_str)

    return counter


def main():
    # # Output: 3
    # n = 39
    # print(persistence(n))

    assert persistence1(39) == 3
    assert persistence1(4) == 0
    assert persistence1(25) == 2
    assert persistence1(999) == 4

    assert persistence2(39) == 3
    assert persistence2(4) == 0
    assert persistence2(25) == 2
    assert persistence2(999) == 4


if __name__ == '__main__':
    main()

