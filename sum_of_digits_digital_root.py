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




def main():
	# Output: 7
	n = 16
	print(digital_root)


    assert digital_root(16) == 7 
    assert digital_root(456) == 6

if __name__ == '__main__':
	main()

