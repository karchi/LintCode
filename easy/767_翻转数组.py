#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 767. 翻转数组,题目地址：https://www.lintcode.com/problem/reverse-array/description
# 原地翻转给出的数组 nums。原地意味着你不能使用额外空间
# 样例:
# 给出 nums = [1,2,5]
# 返回 [5,2,1]
'''


import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        nums = [1,2,5]
        result = self.solutionCase.reverseArray(nums)
        expect = [5,2,1]
        self.assertEqual(nums, expect)
        
    def test_1(self):
        nums = [5,1]
        result = self.solutionCase.reverseArray(nums)
        expect =  [1,5]
        self.assertEqual(nums, expect)
        
    def test_2(self):
        nums = []
        result = self.solutionCase.reverseArray(nums)
        expect = []
        self.assertEqual(nums, expect)
        
        
class Solution:
    """
    @param nums: a integer array
    @return: nothing
    """
    def reverseArray(self, nums):
        for i in range(len(nums)//2):
            nums[i], nums[-i-1] = nums[-i-1], nums[i]
        return None


if __name__ == '__main__':
    unittest.main()
