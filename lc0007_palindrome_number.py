"""Leetcode 7. Palindrome Number
Easy

URL: https://leetcode.com/problems/palindrome-number/

Determine whether an integer is a palindrome. An integer is a palindrome 
when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it 
becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
Coud you solve it without converting the integer to a string?
"""


class Solution(object):
    def isPalindrome(self, x):  # faster
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        if x_str[::-1] == x_str:
            return True
        else:
            return False


class Solution(object):
    def isPalindrome(self, x):
        result = []
        if x < 0:
            return False
        while x != 0:
            num = divmod(x, 10)
            x_div = num[0]    #12, 1, 0
            x_mod = num[1]     #1, 2, 1
            x = x_div
            result.append(x_mod)
        if result != result[::-1]:
            return False
        else:
            return True


class Solution1(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        xx = x
        y = 0
        while xx != 0:
            x_div, x_mod = divmod(xx, 10)
            y = y * 10 + x_mod
            xx = x_div
        if y == x:
            return True
        return False


def main():
    # Output: True
    x = 121
    print(Solution().isPalindrome(x))

    # Output: False
    x = -121
    print(Solution().isPalindrome(x))

    # Output: False
    x = 10
    print(Solution().isPalindrome(x))

    # Output: True
    x = 262
    print(Solution().isPalindrome(x))


if __name__ == '__main__':
    main()

