#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Majority Element,题目地址：https://www.lintcode.com/problem/majority-element/
# 给定一个整型数组，找出主元素，它在数组中的出现次数严格大于数组元素个数的二分之一。
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test1(self):
        self.assertEqual(Solution.majorityNumber(self, [1,1,1,1,2,2,2]), 1)
    def test2(self):
        self.assertEqual(Solution.majorityNumber(self, [1, 2, 1, 2]), None)


class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        numbers = set(nums)
        half = len(nums) / 2
        res = None
        for i in numbers:
            if nums.count(i) > half:
                res = i
                break
        return res



    
if __name__ == '__main__':
    unittest.main()


