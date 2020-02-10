"""Complete The Pattern #1
7 kyu

URL: https://www.codewars.com/kata/5572f7c346eb58ae9c000047/train/python

Task: You have to write a function pattern which returns the following 
Pattern(See Pattern & Examples) upto n number of rows.

Note:Returning the pattern is not the same as Printing the pattern.
Rules/Note:
If n < 1 then it should return "" i.e. empty string.
There are no whitespaces in the pattern.
Pattern:
1
22
333
....
.....
nnnnnn
"""


def pattern(n):
    lst = []

    if n < 1:
        return ""

    for i in range(1, n + 1):
        lst.append(str(i) * i)
        if i != n:
            lst.append("\n")
    return "".join(lst)


def main():
    # Output:"1"
    # n = 1
    # print(pattern(n))

    assert pattern(1) == "1"
    assert pattern(2) == "1\n22"
    assert pattern(5) == "1\n22\n333\n4444\n55555"


if __name__ == '__main__':
    main()


