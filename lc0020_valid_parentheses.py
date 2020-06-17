"""Leetcode 20. Valid Parentheses
Easy

URL: https://leetcode.com/problems/valid-parentheses/

Given a string containing just the characters '(', ')', '{', '}', '[' and
']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        dic = {
            "(": 1,
            ")": -1,
            "{": 2,
            "}": -2,
            "[": 3,
            "]": -3
        }

        chars = list(s)
        n = len(s)
        count = 0
        for i in range(n):
            count += dic[s[i]]
        if count:
            return False

        while n >= 2:
            for i in range(n - 1):
                if dic[chars[i]] + dic[chars[i + 1]] == 0:
                    chars = [chars[j] for j in range(n) 
                             if j not in [i, i + 1]]
                    n = len(chars)
                    break
                elif (i == n - 2 
                      and dic[chars[i]] + dic[chars[i + 1]] != 0):
                    return False

        if not chars:
            return True
        else:
            return False
        

class Solution(object):
    def isValid(self, s):
        
        if not s:
            return True

        stack = [] 
        dic = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            if c in dic:
                if not (stack and stack.pop() == dic[c]):
                    return False
            else:
                stack.append(c)

        return not stack


class Solution1(object):
    def isValid(self, s):
        
        open_close_dic = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        open_set = ('([{')
        close_set = (')]}')
        stack = []

        for c in s:
            if c in open_set:
                stack.append(c)
                continue
            if c in close_set:
                if not stack:
                    return False
                stack_pop = stack.pop()

                if open_close_dic[stack_pop] != c:
                    return False
        if not stack:
            return True
        else:
            False

    
def main():
    # Output: true
    s = "()"
    print(Solution().isValid(s))

    # Output: true
    s = "()[]{}"
    print(Solution().isValid(s))

    # Output: false
    s = "(]"
    print(Solution().isValid(s))

    # Output: false
    s = "([)]"
    print(Solution().isValid(s))

    # Output: true
    s = "{[][]}"
    print(Solution().isValid(s))

    # Output: true
    s = "({[]}[][])" 
    print(Solution().isValid(s))


if __name__ == '__main__':
    main()

