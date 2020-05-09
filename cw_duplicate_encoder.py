"""Codewars: Duplicate Encoder
6 kyu

URL:https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

The goal of this exercise is to convert a string to a new string where 
each character in the new string is "(" if that character appears only 
once in the original string, or ")" if that character appears more than 
once in the original string. Ignore capitalization when determining if 
a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
Notes

Assertion messages may be unclear about what they display in some 
languages. If you read "...It Should encode XXX", the "XXX" is the 
expected result, not the input!
"""


def duplicate_encode(word):
    dic = dict()
    lst = []
    for i in word.lower():
        dic[i] = dic.get(i, 0) + 1
    for i in word.lower():
        if dic[i] > 1:
            lst.append(')')
        else:
            lst.append('(')
    return ''.join(lst)


def duplicate_encode1(word):
    lst = []
    for i in word.lower():
        if word.lower().count(i) > 1:
            lst.append(')')
        else:
            lst.append('(')
    return ''.join(lst)


def duplicate_encode2(word):
    return ''.join(['(' if word.lower().count(i) == 1 else ')' for i in word.lower()])


def main():
    # # Output: "((("
    # word = "din"
    # print(duplicate_encode(word))

    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())"
    assert duplicate_encode("(( @") == "))(("

    assert duplicate_encode1("din") == "((("
    assert duplicate_encode1("recede") == "()()()"
    assert duplicate_encode1("Success") == ")())())"
    assert duplicate_encode1("(( @") == "))(("

    assert duplicate_encode2("din") == "((("
    assert duplicate_encode2("recede") == "()()()"
    assert duplicate_encode2("Success") == ")())())"
    assert duplicate_encode2("(( @") == "))(("

if __name__ == '__main__':
    main()

