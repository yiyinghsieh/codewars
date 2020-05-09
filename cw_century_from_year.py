"""Codewars: Codewars: Century From Year
8 kyu

URL: https://www.codewars.com/kata/century-from-year/train/python

The first century spans from the year 1 up to and including the year 100, 
The second - from the year 101 up to and including the year 200, etc.

Task :
Given a year, return the century it is in.

centuryFromYear(1705)  returns (18)
centuryFromYear(1900)  returns (19)
centuryFromYear(1601)  returns (17)
centuryFromYear(2000)  returns (20)
"""


from __future__ import division
from __future__ import print_function


def century(year):
    import math
    return math.ceil(year / 100)
    

def main():
    # Output:
    year = 1705
    print(century(year))


if __name__ == '__main__':
    main()



