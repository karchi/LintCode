#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 101. 删除排序数组中的重复数字 II，题目地址：https://www.lintcode.com/problem/remove-duplicates-from-sorted-array-ii/description
# 给你一个排序数组，删除其中的重复元素，使得每个数字最多出现两次，返回新的数组的长度。
# 如果一个数字出现超过2次，则这个数字最后保留两个。
# 需要在原数组中操作
# 样例:
# 样例 1:	输入: []	输出: 0
# 样例 2:	输入:  [1,1,1,2,2,3]	输出: 5。 样例解释: 长度为 5，数组为：[1,1,2,2,3]
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.removeDuplicates([])
        expect = 0
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.removeDuplicates([1,1,1,2,2,3])
        expect = 5
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.removeDuplicates([-8,0,1,2,3])
        expect = 5
        self.assertEqual(result, expect)


class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums)-2:
            if nums[i] == nums[i+2]:
                del nums[i]
            else:
                i += 1
        return len(nums)


if __name__ == '__main__':
    unittest.main()
