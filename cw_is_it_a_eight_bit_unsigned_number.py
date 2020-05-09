"""Codewars: Regexp Basics - is it a eight bit unsigned number?
7 kyu

URL: https://www.codewars.com/kata/567e8f7b4096f2b4b1000005/train/python

Implement String#eight_bit_number?, which should return true if given 
object is a number representable by 8 bit unsigned integer (0-255), 
false otherwise.

It should only accept numbers in canonical representation, so no 
leading +, extra 0s, spaces etc.
"""


def eight_bit_number(n):
    if n.isdigit():
        if int(n[0]) == 0 and int(len(n)) > 1:
            return False
        elif int(n) < 0 or int(n) >= 256:
            return False        
        else:
            return True
    else:
        return False


def main():
    # Output: False
    n = "256"
    print(eight_bit_number(n))
   
    # def sample_tests():
    #     tests = [
    #         ("",    False),
    #         ("0",   True),
    #         ("00",  False),
    #         ("55",  True),
    #         ("042", False),
    #         ("123", True),
    #         ("255", True),
    #         ("256", False),
    #         ("999", False),
    #         ("-1",  False)
    #     ]
        # for s, expected in tests:
        #     test.assert_equals(eight_bit_number(s), expected)


if __name__ == '__main__':
    main()

