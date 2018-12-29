#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 1320. 包含重复值么,题目地址：https://www.lintcode.com/problem/contains-duplicate/description
# 给定一个整数数组，查找数组是否包含任何重复项。
# 样例：给定nums =[1,1]，返回true。
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.containsDuplicate([1,1])
        expect = True
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.containsDuplicate([1,2])
        expect = False
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.containsDuplicate([1,2,3,2])
        expect = True
        self.assertEqual(result, expect)
    

class Solution:
    """
    @param nums: the given array
    @return: if any value appears at least twice in the array
    """
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)


if __name__ == '__main__':
    unittest.main()

