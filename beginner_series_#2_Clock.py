"""Codewars: Beginner Series #2 Clock
8 kyu

URL: https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a/train/python

Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.

Your task is to make 'Past' function which returns time converted to miliseconds.

Example:
past(0, 1, 1) == 61000
Note! h, m and s will be only Natural numbers! Waiting for translations and 
Feedback! Thanks!
"""


def past(h, m, s):
    h = h * 60 * 60 * 1000
    m = m * 60 * 1000
    s = s * 1000
    return (h + m + s)



def main():
    # h, m, s = (0, 1, 1)
    # print(past(h, m, s))

    assert past(0,1,1) == 61000
    assert past(1,1,1) == 3661000
    assert past(0,0,0) == 0
    assert past(1,0,1) == 3601000
    assert past(1,0,0) == 3600000


if __name__ == '__main__':
    main()

