#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 868. 子数组的最大平均值,题目地址：https://www.lintcode.com/problem/maximum-average-subarray-i/description
# 给定一个由n个整数组成的数组，找到给定长度k的连续子数组，该子数组具有最大平均值。你需要输出最大平均值。
# 1 <= k <= n <= 30,000.
# 给定数组的元素将在范围[-10,000, 10,000]。
'''


import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.findMaxAverage([1,12,-5,-6,50,3], 4)
        expect = 12.75
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.findMaxAverage([0], 1)
        expect = 0
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.findMaxAverage([1,2,3], 3)
        expect = 2
        self.assertEqual(result, expect)
    

class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the maximum average value
    """
    def findMaxAverage(self, nums, k):
        max = sum(nums[:k])
        for i in range(len(nums)-k+1):
            sum_i = sum(nums[i:i+k])
            if sum_i > max:
                max = sum_i
        return max / k


if __name__ == '__main__':
    unittest.main()

