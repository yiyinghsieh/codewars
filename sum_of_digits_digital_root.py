"""Sum of Digits / Digital Root

6 kyu

URL:https://www.codewars.com/kata/541c8630095125aba6000c00

In this kata, you must create a digital root function.
A digital root is the recursive sum of all the digits in a number. 
Given n, take the sum of the digits of n. If that value has more than 
one digit, continue reducing in this way until a single-digit number is 
produced. This is only applicable to the natural numbers.

Here's how it works:

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29 ...
=> 2 + 9
=> 11 ...
=> 1 + 1
=> 2
"""


def digital_root(n):
    sum_i = 0
    for i in str(n):
        sum_i += int(i)
    length = len(str(sum_i))
    
    if length < 2:
        return sum_i
    else:
        while length > 1:
            sum_ii = 0
            for j in str(sum_i):
                sum_ii += int(j)
            length = len(str(sum_ii))
    return sum_ii


def digital_root1(n):
    while n > 10:
        n = sum([int(i) for i in str(n)])
    return n


def digital_root2(n):
    while n > 10:
        sum_n = 0
        for i in str(n):
            sum_n += int(i)
            n = sum_n
    return n


def main():
    # # Output: 7
    # n = 456
    # print(digital_root(n))

    assert digital_root(16) == 7 
    assert digital_root(456) == 6

    assert digital_root1(16) == 7 
    assert digital_root1(456) == 6

    assert digital_root2(16) == 7 
    assert digital_root2(456) == 6

if __name__ == '__main__':
    main()

