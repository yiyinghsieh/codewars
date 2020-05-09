"""Codewars: Tidy Number (Special Numbers Series #9)
7 kyu

URL: https://www.codewars.com/kata/5a87449ab1710171300000fd/train/python

Definition
A Tidy number is a number whose digits are in non-decreasing order.

Task
Given a number, Find if it is Tidy or not .

Notes
Number passed is always Positive .
Return the result as a Boolean

Input >> Output Examples
tidyNumber (12) ==> return (true)
Explanation:
The number's digits { 1 , 2 } are in non-Decreasing Order (i.e) 1 <= 2 .
"""


def tidyNumber1(n):
    n_lst = list(str(n))
    n_sort = sorted(n_lst)
    if n_lst == n_sort:
        return True
    else:
        return False


def tidyNumber2(n):
    n = str(n)
    for c in range(len(n) - 1):
        if n[c] > n[c + 1]:
            return False
    return True
        

def main():
    # Output: True
    # n = '2789'
    # print(tidyNumber(n))
    tidyNumber = tidyNumber2
    assert tidyNumber(12) == True
    assert tidyNumber(102) == False
    assert tidyNumber(9672) == False
    assert tidyNumber(2789) == True


if __name__ == '__main__':
    main()

