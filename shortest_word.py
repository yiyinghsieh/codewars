"""Shortest Word
7 kyu

URL: https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python

Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different 
data types.
"""


def find_short(s):
    min_len = 10
    s_split = s.split()
    for word in s_split:
        word_lend = len(word)
        if word_lend < min_len:
            min_len = word_lend
    return min_len


def find_short(s):
    lst = []
    s_split = s.split()
    for word in s_split:
        word_lend = lst.append(len(word))
    return min(lst)


def find_short(s):
    return min([len(l) for l in s.split()])


def main():
    # Output: 3
    # s = "bitcoin take over the world maybe who knows perhaps"
    # print(find_short(s))

    assert find_short("bitcoin take over the world maybe who knows perhaps") == 3
    assert find_short("turns out random test cases are easier than writing out basic ones") == 3
    assert find_short("lets talk about javascript the best language") == 3
    assert find_short("i want to travel the world writing code one day") == 1
    assert find_short("Lets all go on holiday somewhere very cold") == 2


if __name__ == '__main__':
    main()


