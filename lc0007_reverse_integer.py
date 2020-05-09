"""Leetcode 7. Reverse Integer
Easy

URL: https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose
of this problem, assume that your function returns 0 when the reversed
integer overflows.
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # while x % 10 == 0:
        #     x = x // 10
        if x > 0:
            x = int(str(x)[::-1])
        elif x < 0 :
            x = -int(str(-x)[::-1])

        return x if -2 ** 31 < x < 2 ** 31 else 0


def main():
    # Output: 321
    x = 123
    print(Solution().reverse(x))

    # Output: -321
    x = -123
    print(Solution().reverse(x))

    # Output: 21
    x = 120
    print(Solution().reverse(x))

    # Output: -21
    x = -12000
    print(Solution().reverse(x))


if __name__ == '__main__':
    main()


