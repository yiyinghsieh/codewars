"""Leetcode 7. Two Sum
Easy

URL: https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that 
they add up to a specific target.

You may assume that each input would have exactly one solution, and you 
may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        l_half = l // 2
        num_sort = sorted(nums)
        
        if target < num_sort[l_half]:
            for i in range(l):
                for ii in range(l):
                    if i == ii:
                        continue
                    if num_sort[i] + num_sort[ii] == target:
                        newnum = [num_sort[i], num_sort[ii]]
                        ans = []
                        for ii in newnum:
                            for i, c in enumerate(nums):
                                if ii == c and i not in ans:
                                    ans += [i]
                                    break 
                        return sorted(ans)
        elif target > num_sort[l_half] * 2:
            for i in range(l):
                for ii in range(l):
                    if i == ii:
                        continue
                    if num_sort[-i] + num_sort[-ii] == target:
                        newnum = [num_sort[-i]] + [num_sort[-ii]]
                        ans = []
                        for ii in newnum:
                            for i, c in enumerate(nums):
                                if ii == c and i not in ans:
                                    ans += [i]
                                    break 
                        return sorted(ans)
        else:
            for i in range(l):
                for ii in range(l):
                    if i == ii:
                        continue
                    if num_sort[i] + num_sort[ii] == target:
                        newnum = [num_sort[i]] + [num_sort[ii]]
                        ans = []
                        for ii in newnum:
                            for i, c in enumerate(nums):
                                if ii == c and i not in ans:
                                    ans += [i]
                                    break 
                        return sorted(ans)


class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution1(object):
    def twoSum(self, nums, target):
        dic = {}
        for i, c in enumerate(nums):
            if c in dic:
                return [dic[c], i]
            dic[target - c] = i


def main():
    # Output: [0, 1]
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))

    # Output: [1, 2]
    nums = [2, 5, 7, 7, 11]
    target = 12
    print(Solution().twoSum(nums, target))
   
    # Output: [0, 1]
    nums = [3, 3]
    target = 6
    print(Solution().twoSum(nums, target))

    # Output: [1, 2]
    nums = [3, 2, 4]
    target = 6
    print(Solution().twoSum(nums, target))
    
    # Output: [3, 8]
    nums = [3, 2, 4, 6, 7, 4, 3, 6, 9, 9]
    target = 15
    print(Solution1().twoSum(nums, target))

    # Output: [28, 45]
    nums = [230,863,916,585,981,404,316,785,88,12,70,435,384,778,887,755,740,337,86,92,325,422,815,650,920,125,277,336,221,847,168,23,677,61,400,136,874,363,394,199,863,997,794,587,124,321,212,957,764,173,314,422,927,783,930,282,306,506,44,926,691,568,68,730,933,737,531,180,414,751,28,546,60,371,493,370,527,387,43,541,13,457,328,227,652,365,430,803,59,858,538,427,583,368,375,173,809,896,370,789]
    target = 542
    print(Solution1().twoSum(nums, target))


if __name__ == '__main__':
    main()

