"""Consonant value
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





def main():
	# Output: 26
	s = "zodiac"
	print(solve(s))

Test.it("Basic tests")
Test.assert_equals(solve("zodiac"),26)
Test.assert_equals(solve("chruschtschov"),80)
Test.assert_equals(solve("khrushchev"),38)
Test.assert_equals(solve("strength"),57)
Test.assert_equals(solve("catchphrase"),73)
Test.assert_equals(solve("twelfthstreet"),103)
Test.assert_equals(solve("mischtschenkoana"),80)


if __name__ == '__main__':
	main()


