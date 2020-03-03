"""Testing 1-2-3
7 kyu

URL: https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python

Your team is writing a fancy new text editor and you've been tasked with 
implementing the line numbering.
Write a function which takes a list of strings and returns each line 
prepended by the correct number.
The numbering starts at 1. The format is n: string. Notice the colon and 
space in between.

Examples:
number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]
"""


def number(lines):
    # dict: {number->c}
    # list: ['number: c']
    # number_c_d = {i + 1: c for i, c in enumerate(lines)}
    # return number_c_d
    if lines == []:
        return []
    number_c_ls = [str(i + 1) + ': ' + c for i, c in enumerate(lines)]
    return number_c_ls


def main():
    # Output: ["1: a", "2: b", "3: c"]
    # lines = ["a", "b", "c"]
    # print(number(lines))

    assert number([]) == []
    assert number(["a", "b", "c"]) == ["1: a", "2: b", "3: c"]


if __name__ == '__main__':
    main()

    