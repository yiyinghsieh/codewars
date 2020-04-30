"""Reversing a Process
6 kyu

URL:https://www.codewars.com/kata/5dad6e5264e25a001918a1fc/train/python

Suppose we know the process (A) by which a string s has been coded to a 
string r.

The aim of the kata is to decode r to get back the original string s.

Explanation of the known process (A):
data: a string s composed of lowercase letters from a to z and a positive
integer num
we know there is a correspondence between abcde...uvwxyzand 0, 1, 2 ..., 
23, 24, 25 : 0 <-> a, 1 <-> b ...
if c is a character of s whose corresponding number is x, apply to x the
function f: x-> f(x) = num * x % 26, then find ch the corresponding 
character of f(x)
Accumulate all these ch in a string r.
concatenate num and r and return the result.

Example:
code("mer", 6015) -> "6015ekx"
m <-> 12, 12 * 6015 % 26 == 4, 4 <-> e
e <-> 4, 4 * 6015 % 26 == 10, 10 <-> k
r <-> 17, 17 * 6015 % 26 == 23, 23 <-> x
We get "ekx" hence "6015ekx"

Task
A string s has been coded to a string r by the above process (A). 
Write a function r -> decode(r) to get back s whenever it is possible.

Indeed it can happen that the decoding is impossible when positive 
integer num has not been correctly chosen. In that case return 
"Impossible to decode".

Example:
decode("6015ekx") -> "mer"
decode("5057aan") -> "Impossible to decode"
Note
Please could you ask before translating : some translations are already 
written.
"""


def decode(r):
    import re
    import string
    num = re.findall('[0-9]+', r)[0]
    words = re.findall('[a-z]+', r)[0]
    lst = []

    for i in words:
        x = (ord(i) - ord('a'))
        for ii in range(26):
            if ii * int(num) % 26 == x:
                lst.append(ii)
    result = []
    for j in lst:
        for i, c in enumerate(string.ascii_lowercase):
            if j == i:
                result.append(c)
    if len(result) > len(words):
        return 'Impossible to decode'
    return ''.join(result)


def main():
    # Output: "uogbucwnddunktsjfanzlurnyxmx"
    r = "1273409kuqhkoynvvknsdwljantzkpnmfgf"
    print(decode(r))

# @test.describe('Tests')
     
# def fixed_tests():
#     def testing_decode(s, exp):
#         actual = decode(s)
#         Test.assert_equals(actual, exp)
#     @test.it('Basic Tests')
#     def basic_tests1():
#         testing_decode("1273409kuqhkoynvvknsdwljantzkpnmfgf", "uogbucwnddunktsjfanzlurnyxmx")
#         testing_decode("761328qockcouoqmoayqwmkkic", "Impossible to decode")
#         testing_decode("1544749cdcizljymhdmvvypyjamowl", "mfmwhbpoudfujjozopaugcb")
#         testing_decode("1122305vvkhrrcsyfkvejxjfvafzwpsdqgp", "rrsxppowmjsrclfljrajtybwviqb")
        

if __name__ == '__main__':
    main()

