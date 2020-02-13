"""Alphabetical Addition
7 kyu

URL: https://www.codewars.com/kata/5d50e3914861a500121e1958/train/python

Your task is to add up letters to one letter.
The function will be given a variable amount of arguments, each one being 
a letter to add.

Notes:
Letters will always be lowercase.
Letters can overflow (see second to last example of the description)
If no letters are given, the function should return 'z'

Examples:
add_letters('a', 'b', 'c') = 'f'
add_letters('a', 'b') = 'c'
add_letters('z') = 'z'
add_letters('z', 'a') = 'a'
add_letters('y', 'c', 'b') = 'd' # notice the letters overflowing
add_letters() = 'z'
"""


def add_letters(*letters):
    import string
    add = 0
    a_z = string.ascii_lowercase
    for l in letters:
        for i in range(len(a_z)):
            if l == a_z[i]:
                add += i + 1
    return a_z[add % 26 - 1]


def add_letters(*letters):
    import string
    add = 0
    for l in letters:
        for i , c in enumerate(string.ascii_lowercase):
            if l == c:
                add += i + 1
    return string.ascii_lowercase[add % 26 - 1]


def add_letters(*letters):
    import string
    add = 0
    for l in letters:
        add += ord(l) - ord('a') + 1
    return string.ascii_lowercase[add % 26 - 1]


def add_letters(*letters):
    import string
    add = 0
    letter_idx_d = {c: i + 1 for i, c in enumerate(string.ascii_lowercase)}
    for l in letters:
        add += letter_idx_d[l]
    return string.ascii_lowercase[add % 26 - 1]


def main():
    # Output: 'f'
    letters = 'a', 'b', 'c'
    print(add_letters(*letters))

 #    tests = [
 #        (['a', 'b', 'c'], 'f'),
 #        (['z'], 'z'),
 #        (['a', 'b'], 'c'),
 #        (['c'], 'c'),
 #        (['z', 'a'], 'a'),
 #        (['y', 'c', 'b'], 'd'),
 #        ([], 'z')
 #    ]
 #    for i, o in tests:
 #        str = ', '.join(['"' + s + '"' for s in i])
 #        @test.it("add_letters(" + str + ")")
 #        def fixed_test():
 #            Test.assert_equals(add_letters(*i), o)


if __name__ == '__main__':
    main()

