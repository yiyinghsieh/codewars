"""Odd or Even?
7 kyu

URL: https://www.codewars.com/kata/5949481f86420f59480000e7/train/python

Task:
Given a list of numbers, determine whether the sum of its elements is odd 
or even.
Give your answer as a string matching "odd" or "even".
If the input array is empty consider it as: [0] (array with a zero).

Example:
odd_or_even([0])          ==  "even"
odd_or_even([0, 1, 4])    ==  "odd"
odd_or_even([0, -1, -5])  ==  "even"
Have fun!
"""


def odd_or_even(arr):



def main():

Test.assert_equals(odd_or_even([0, 1, 2]), "odd")
Test.assert_equals(odd_or_even([0, 1, 3]), "even")
Test.assert_equals(odd_or_even([1023, 1, 2]), "even")



if __name__ == '__main__':
	main()