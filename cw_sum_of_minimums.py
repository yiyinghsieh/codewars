"""Codewars: Sum of Minimums!
7 kyu

URL: https://www.codewars.com/kata/5d5ee4c35162d9001af7d699/train/python

Given an 2D list of size m * n. Your task is to find the sum of minimum 
value in each row.

For Example:
[
  [1,2,3,4,5], # minimum value of row is 1
  [5,6,7,8,9], # minimum value of row is 5
  [20,21,34,56,100] # minimum value of row is 20
]
So, the function should return 26 because sum of minimums is as 
1 + 5 + 20 = 26
Note: You will be always given non-empty list containing Positive values.
"""


def sum_of_minimums(numbers):
    num = 0
    for n in numbers:
        n_sorted = sorted(n)
        # for i in range(1):
        num += n_sorted[0]
    return num


def sum_of_minimums2(numbers):
    return sum([min(i) for i in numbers])


def sum_of_minimums3(numbers):
    lst = []
    for i in numbers:
        lst.append(sorted(i)[0])
    return sum(lst)


def main():
    # Output: 9
    # numbers = [ [ 7,9,8,6,2 ], [6,3,5,4,3], [5,8,7,4,5] ]
    # print(sum_of_minimums(numbers))

    assert sum_of_minimums([ [ 7,9,8,6,2 ], [6,3,5,4,3], [5,8,7,4,5] ]) == 9
    assert sum_of_minimums([ [11,12,14,54], [67,89,90,56], [7,9,4,3], [9,8,6,7]]) == 76


if __name__ == '__main__':
    main()

