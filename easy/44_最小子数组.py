#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 44. 最小子数组,题目地址：https://www.lintcode.com/problem/minimum-subarray/description
# 给定一个整数数组，找到一个具有最小和的子数组。返回其最小和。子数组最少包含一个数字
# 样例:给出数组[1, -1, -2, 1]，返回 -3
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.minSubArray([1, -1, -2, 1])
        expect = -3
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.minSubArray([1,4,3])
        expect =  1
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.minSubArray([1])
        expect = 1
        self.assertEqual(result, expect)
        
    def test_3(self):
        result = self.solutionCase.minSubArray([-5,10,-4])
        expect = -5
        self.assertEqual(result, expect)
    

class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        minsum = dp_n = nums.pop(0)
        for item in nums:
            dp_n = item if dp_n >= 0 else dp_n + item
            minsum = min(dp_n, minsum)
        return minsum
            
        
if __name__ == '__main__':
    unittest.main()

