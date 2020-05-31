"""Leetcode 14. Longest Common Prefix
Easy

URL: https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array
of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ''
        result = []
        l = len(strs[0])
        for i, c in enumerate(strs[0]):
            for k in range(1, len(strs)):
                if i >= len(strs[k]) or c != strs[k][i]:
                    return ''.join(result)
            result.append(c)
        return ''.join(result)
        

def main():
    # Output: "fl"
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))

    # Output: "fl"
    strs = ["flower","flow","flight","floor"]
    print(Solution().longestCommonPrefix(strs))

    # Output: "flow"
    strs = ["flower","flow","flow","floweo"]
    print(Solution().longestCommonPrefix(strs))

    # Output: "a"
    strs = ["aa","a"]
    print(Solution().longestCommonPrefix(strs))

    # Output: ""
    strs = ["dog","racecar","car"]
    print(Solution().longestCommonPrefix(strs))

    # Output: "c"
    strs = ["c","c"]
    print(Solution().longestCommonPrefix(strs))

    # Output: "c"
    strs = ["c"]
    print(Solution().longestCommonPrefix(strs))

    # Output: ""
    strs = ["", ""]
    print(Solution().longestCommonPrefix(strs))

    # Output: ""
    strs = []
    print(Solution().longestCommonPrefix(strs))

    # Output: ""
    strs = ["a","b"]
    print(Solution().longestCommonPrefix(strs))

    # Output: ""
    strs = ["a","a","b"]
    print(Solution().longestCommonPrefix(strs))

    # Output: "aa"
    strs = ["aa","aa"]
    print(Solution().longestCommonPrefix(strs))
    
    # Output: "a"
    strs = ["aa","ab"]
    print(Solution().longestCommonPrefix(strs))

    # Output: ""
    strs = ["aa","ba","aa"]
    print(Solution().longestCommonPrefix(strs))


if __name__ == '__main__':
    main()

