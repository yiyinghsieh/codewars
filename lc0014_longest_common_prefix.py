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
        n = len(strs)
        result = []
        count = n

        for i in strs:
            for ii in range(1):
                result.append(i[0])
                print(result)
                if ''.join(result) != i[0]*n:
                    return 'no'
        lst = []
        while count > 1:
            for i in strs:
                for ii in range(count):
                    lst.append(i[ii])
                    # print(lst)
                    if i[:count] == ''.join(lst):
                        return i[:count], ''.join(lst)
                    else:
                        count -= 1

        # print(i[:count], ''.join(result))
        # while count < 5:
            # if ''.join(result) == i[count] * n:
            #     count += 1
            # else:
            #     break
            #     return result
            # return False
            # if i[count] == i[0]:
            #     result.append(i[count])
            #     count += 1
            # else:
            #     break

        # print(result[:2])

            

        # print(''.join(result), i[0] * n)


def main():
    # Output: "fl"
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))

    # # Output: ""
    # strs = ["dog","racecar","car"]
    # print(Solution().longestCommonPrefix(strs))



if __name__ == '__main__':
    main()

