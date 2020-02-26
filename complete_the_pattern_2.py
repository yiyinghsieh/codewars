"""Complete The Pattern #2
7 kyu

URL: https://www.codewars.com/kata/55733d3ef7c43f8b0700007c/train/python

Task:
You have to write a function pattern which returns the following Pattern 
(See Pattern & Examples) upto n number of rows.
Note: 
Returning the pattern is not the same as Printing the pattern.
Rules/Note:
If n < 1 then it should return "" i.e. empty string.
There are no whitespaces in the pattern.

Pattern:
(n)(n-1)(n-2)...4321
(n)(n-1)(n-2)...432
(n)(n-1)(n-2)...43
(n)(n-1)(n-2)...4
...............
..............
(n)(n-1)(n-2)
(n)(n-1)
(n)
Examples:
pattern(4):

4321
432
43
4
"""


def pattern(n):



def main():

Test.assert_equals(pattern(1),"1")
Test.assert_equals(pattern(2),"21\n2")
Test.assert_equals(pattern(5),"54321\n5432\n543\n54\n5")


if __name__ == '__main__':
	main()
















