"""Break camelCase
6 kyu

URL:https://www.codewars.com/kata/5208f99aee097e6552000148/train/python

Complete the solution so that the function will break up camel casing, 
using a space between words.

Example
solution("camelCasing")  ==  "camel Casing"
"""


def solution(s):
    import string
    n = len(s)
    lst = []

    uppercase = set(string.ascii_uppercase)
    for i in range(n):
        if s[i] in uppercase:
            lst.append(' ')
        lst.append(s[i])
    return ''.join(lst)


def main():
    # # Output: "hello World" 
    # s = "helloWorld"
    # print(solution(s))

    # # Output: "break Camel Case" 
    # s = "breakCamelCase"
    # print(solution(s))

    assert solution("helloWorld") == "hello World"
    assert solution("camelCase") == "camel Case"
    assert solution("breakCamelCase") == "break Camel Case"


if __name__ == '__main__':
    main()

