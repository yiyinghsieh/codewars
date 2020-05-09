"""Codewars: Sum of odd numbers
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
    """
    Time complexity: O(1+2+...+n)=O(n^2).
    Space complexity: O(n^2).
    """
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


def row_sum_odd_numbers2(n):
    """
    Time complexity: O(1+2+...+n)=O(n^2).
    Space complexity: O(n).
    """
    # Edge case.
    if n == 1:
        return 1

    n_odds = sum([i for i in range(1, n + 1)]) - n

    idx = 1
    odd = 1
    lst = []
    while idx != n_odds:
        odd += 2
        idx += 1

    for j in range(1, n + 1):
        odd += 2
        lst.append(odd)
    return sum(lst)


def row_sum_odd_numbers3(n):
    """
    Time complexity: O(n).
    Space complexity: O(n).
    """
    start_odd = n * (n - 1) + 1

    row = []
    for i in range(1, n + 1):
        row.append(start_odd + (i - 1) * 2)
    return sum(row)


def row_sum_odd_numbers4(n):
    """
    Time complexity: O(n).
    Space complexity: O(n).
    """
    start_odd = n * (n - 1) + 1
    end_odd = start_odd + 2 * (n - 1)
    # return sum([odd for odd in range(start_odd, end_odd + 1, 2)])
    return sum(range(start_odd, end_odd + 1, 2))


def row_sum_odd_numbers5(n):
    """
    Time complexity: O(1).
    Space complexity: O(1).
    """
    return n ** 3


def main():
    # # Output: 1
    # n = 3
    # print(row_sum_odd_numbers(n))

    assert row_sum_odd_numbers1(1) == 1
    assert row_sum_odd_numbers1(2) == 8
    assert row_sum_odd_numbers1(13) == 2197
    assert row_sum_odd_numbers1(19) == 6859
    assert row_sum_odd_numbers1(41) == 68921

    assert row_sum_odd_numbers2(1) == 1
    assert row_sum_odd_numbers2(2) == 8
    assert row_sum_odd_numbers2(13) == 2197
    assert row_sum_odd_numbers2(19) == 6859
    assert row_sum_odd_numbers2(41) == 68921

    assert row_sum_odd_numbers3(1) == 1
    assert row_sum_odd_numbers3(2) == 8
    assert row_sum_odd_numbers3(13) == 2197
    assert row_sum_odd_numbers3(19) == 6859
    assert row_sum_odd_numbers3(41) == 68921

    assert row_sum_odd_numbers4(1) == 1
    assert row_sum_odd_numbers4(2) == 8
    assert row_sum_odd_numbers4(13) == 2197
    assert row_sum_odd_numbers4(19) == 6859
    assert row_sum_odd_numbers4(41) == 68921

    assert row_sum_odd_numbers5(1) == 1
    assert row_sum_odd_numbers5(2) == 8
    assert row_sum_odd_numbers5(13) == 2197
    assert row_sum_odd_numbers5(19) == 6859
    assert row_sum_odd_numbers5(41) == 68921


if __name__ == '__main__':
    main()

