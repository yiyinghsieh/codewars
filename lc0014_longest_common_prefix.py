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
        

def main():
	# Output: "fl"
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))

    # Output: ""
    strs = ["dog","racecar","car"]
    print(Solution().longestCommonPrefix(strs))



if __name__ == '__main__':
	main()

