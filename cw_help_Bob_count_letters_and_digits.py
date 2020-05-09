"""Codewars: Help Bob count letters and digits
7 kyu

URL: https://www.codewars.com/kata/5738f5ea9545204cec000155/train/python

Bob is a lazy man.
He needs you to create a method that can determine how many letters and 
digits are in a given string.

Example:
"hel2!lo" --> 6
"wicked .. !" --> 6
"!?..A" --> 1
"""


def count_letters_and_digits(s):
    count = 0
    for i in s:
        if i.isalpha() or i.isdigit():
            count += 1
    return count


def main():
    # Output: 7
    # s = 'n!!ice!!123'
    # print(count_letters_and_digits(s))

    assert count_letters_and_digits('n!!ice!!123') == 7
    assert count_letters_and_digits('de?=?=tttes!!t') == 8
    assert count_letters_and_digits('') == 0
    assert count_letters_and_digits('!@#$%^&`~.') == 0
    assert count_letters_and_digits('u_n_d_e_r__S_C_O_R_E') == 10


if __name__ == '__main__':
    main()

