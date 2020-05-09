"""Codewars: Consonant value
6 kyu

URL:https://www.codewars.com/kata/59c633e7dcc4053512000073/train/python

Given a lowercase string that has alphabetic characters only and no 
spaces, return the highest value of consonant substrings. Consonants are
any letters of the alphabet except "aeiou".

We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

For example, for the word "zodiacs", let's cross out the vowels. 
We get: "z o d ia cs"

-- The consonant substrings are: "z", "d" and "cs" and the values are 
z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.
solve("zodiacs") = 26

For the word "strength", solve("strength") = 57
-- The consonant substrings are: "str" and "ngth" with values "str" 
= 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.

For C: do not mutate input.
More examples in test cases. Good luck!
"""


def solve(s):
    import string
    a_z = string.ascii_lowercase
    vowels = 'aeiou'
    s_lst = []
    for i in s:
        if i not in vowels:
            s_lst.append(i)
        else:
            s_lst.append('')

    s_max = []
    s_sum = 0
    for j in s_lst:
        for i, c in enumerate(a_z):
            if j == c:
                s_sum += i + 1
                s_max.append(s_sum)
            elif j == '':
                s_sum = 0
    return(max(s_max))

def solve1(s):
    max_s = 0
    add_s = 0
    vowels = 'aeiou'
    for i in s:
        if i not in vowels:
            add_s += ord(i) - 97 + 1
        else:
            add_s = 0
        if add_s > max_s:
            max_s = add_s
    return max_s


def main():
    # # Output: 26
    # s = "zodiac"
    # print(solve(s))

    assert solve("zodiac") == 26
    assert solve("chruschtschov") == 80
    assert solve("khrushchev") == 38
    assert solve("strength") == 57
    assert solve("catchphrase") == 73
    assert solve("twelfthstreet") == 103
    assert solve("mischtschenkoana") == 80

    assert solve1("zodiac") == 26
    assert solve1("chruschtschov") == 80
    assert solve1("khrushchev") == 38
    assert solve1("strength") == 57
    assert solve1("catchphrase") == 73
    assert solve1("twelfthstreet") == 103
    assert solve1("mischtschenkoana") == 80


if __name__ == '__main__':
    main()

