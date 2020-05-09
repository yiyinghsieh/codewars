"""Codewars: Break camelCase
6 kyu

URL:https://www.codewars.com/kata/5208f99aee097e6552000148/train/python

Complete the solution so that the function will break up camel casing, 
using a space between words.

Example
solution("camelCasing")  ==  "camel Casing"
"""


def solution(s):
    import string
    
    uppercase = set(string.ascii_uppercase)
    i = 0
    while i < len(s):
        # 'helloWorld' => 'hello World'
        #  0123456789
        if s[i] in uppercase:
            s = s[:i] + ' ' + s[i:]
            i += 1
        i += 1

    return s


def solution1(s):
    lst = []
    for i in s:
        if i.isupper():
            lst.append(' ')
        lst.append(i)
    return ''.join(lst)


def solution2(s):
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

    assert solution1("helloWorld") == "hello World"
    assert solution1("camelCase") == "camel Case"
    assert solution1("breakCamelCase") == "break Camel Case"

    assert solution2("helloWorld") == "hello World"
    assert solution2("camelCase") == "camel Case"
    assert solution2("breakCamelCase") == "break Camel Case"



if __name__ == '__main__':
    main()

