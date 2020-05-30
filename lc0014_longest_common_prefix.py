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
        if not strs or not strs[0]:
            return ''
        if len(strs) == 1:
            return strs[0]

        l = len(strs)
        l_word = len(strs[0])
        # print(l_word)
        n = 0
        while n <= l_word -1:
            word = strs[1][n]#######
            for i in range(1, l):
                a = len(strs[i])
                print(a-1, n, a)
                if n == a-1 and word == strs[i][n]:
                    return strs[i][:n+1]
                if word == strs[i][n]:
                    # print(word, strs[i][n])
                    continue
                else:
                    print(strs[i][:n])
                    print(strs[0][:n])
                    return strs[0][:n]
            n += 1


        # if not strs or not strs[0]:
        #     return ''

        # if len(strs) == 1:
        #     return strs[0]

        # n = len(strs)
        # c = 1
        # cc = 1
        # lst = []

        # for i in strs:
        #     lst.append(i[0])
        # if ''.join(lst) != lst[0]*n:
        #     return ''
        # elif ''.join(lst) == lst[0]*n and len(i) ==1:
        #     return lst[0]

        # while c <= 8:#######
        #     result = []
        #     for i in strs:
        #         for ii in range(c):
        #             result.append(i[ii])
        #         if len(i) >= c and ''.join(result) == i[:ii]*n:
        #             c += 1
        #         if len(i) >= c or ''.join(result) != i[:ii]*n:

        #             # print(result)
        #             return i[:ii]
        #           # return i[:ii]
        #               # return 'a'
        #         else:
        #             return strs[0]

        # # if len(i) == c and ''.join(result) == i[:ii]*n:
        # return strs[0]
                    

def main():
    # # Output: "fl"
    # strs = ["flower","flow","flight"]
    # print(Solution().longestCommonPrefix(strs))

    # # Output: "fl"
    # strs = ["flower","flow","flight","floor"]
    # print(Solution().longestCommonPrefix(strs))

    # # Output: "flow"
    # strs = ["flower","flow","flow","floweo"]
    # print(Solution().longestCommonPrefix(strs))

    # # Output: ""
    # strs = ["dog","racecar","car"]
    # print(Solution().longestCommonPrefix(strs))

    # # Output: "c"
    # strs = ["c","c"]
    # print(Solution().longestCommonPrefix(strs))

    # # Output: "c"
    # strs = ["c"]
    # print(Solution().longestCommonPrefix(strs))

    # # Output: ""
    # strs = [""]
    # print(Solution().longestCommonPrefix(strs))

    # # Output: ""
    # strs = []
    # print(Solution().longestCommonPrefix(strs))

    # Output: ""
    strs = ["a","b"]  #####expection 
    print(Solution().longestCommonPrefix(strs))

    print(strs[i][:n])
    print(strs[0][:n])
    return strs[0][:n]


    # # Output: "aa"
    # strs = ["aa","aa"]
    # print(Solution().longestCommonPrefix(strs))

    # # Output: ""
    # strs = ["aa","ba","aa"]
    # print(Solution().longestCommonPrefix(strs))




if __name__ == '__main__':
    main()

