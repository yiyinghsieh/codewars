"""Persistent Bugger
6 kyu

URL: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

Write a function, persistence, that takes in a positive parameter num 
and returns its multiplicative persistence, which is the number of 
times you must multiply the digits in num until you reach a single 
digit.

For example:
persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

persistence(4) => 0   # Because 4 is already a one-digit number.
 
persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit

persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

persistence(4) # returns 0, because 4 is already a one-dig
"""


def persistence(n):


def main():
	# Output: 3
	n = 39
	print(persistence(n))

    assert persistence(39) == 3
    assert persistence(4) == 0
    assert persistence(25) == 2
    assert persistence(999) == 4


if __name__ == '__main__':
	main()

