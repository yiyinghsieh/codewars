"""Codewars: String ends with?
7 kyu

URL: https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python

Complete the solution so that it returns true if the first argument(string) 
passed in ends with the 2nd argument (also a string).

Examples:
solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
"""


def solution(string, ending):
    end_len = len(ending)
    str_len = len(string)
    str_end = str_len - end_len
    lst = []
    for i in range(str_end, str_len):
        lst.append(string[i])
    if ending == ''.join(lst) or ending == '':
        return True
    else:
        return False


def solution(string, ending):
    if ending == string[len(string) - len(ending):]:
        return True
    else:
        return False


def solution(string, ending):
    return string.endswith(ending)
    

def main():
    # Output: True
    # string, ending = 'abcde', 'cde'
    # print(solution(string, ending))

    assert solution('abcde', 'cde') == True
    assert solution('abcde', 'abc') == False
    assert solution('abcde', '') == True

if __name__ == '__main__':
    main()

