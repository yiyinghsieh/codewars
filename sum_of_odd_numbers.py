"""Sum of odd numbers
7 kyu

URL: https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python

Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8
"""


def row_sum_odd_numbers1(n):
    # Edge case.
    if n == 1:
        return 1

    n_odds = sum([i for i in range(1, n + 1)])

    idx = 1
    odd = 1
    lst = []
    while idx != n_odds:
        odd += 2
        lst.append(odd)
        idx += 1

    return sum(lst[-n:])


def main():
    # # Output: 1
    # n = 1
    # print(row_sum_odd_numbers(n))

    assert row_sum_odd_numbers1(1) == 1
    assert row_sum_odd_numbers1(2) == 8
    assert row_sum_odd_numbers1(13) == 2197
    assert row_sum_odd_numbers1(19) == 6859
    assert row_sum_odd_numbers1(41) == 68921


if __name__ == '__main__':
    main()




