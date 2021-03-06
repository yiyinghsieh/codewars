"""Codewars: Complete The Pattern #2
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
    end = 0
    stair = 0
    lst = []
    if n < 1:
        return ''
    while stair != n:    
        for i in range(n, end, -1):
            lst.append(str(i))
        if end + 1 != n:
            lst.append("\n") 
        end += 1
        stair += 1
    return ''.join(lst)


def main():
    assert pattern(1) == "1"
    assert pattern(2) == "21\n2"
    assert pattern(5) == "54321\n5432\n543\n54\n5"


if __name__ == '__main__':
    main()

