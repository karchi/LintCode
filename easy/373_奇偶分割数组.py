#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 373.奇偶分割数组,题目地址：https://www.lintcode.com/problem/partition-array-by-odd-and-even/description
# 分割一个整数数组，使得奇数在前偶数在后。
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_A(self):
        A = [1, 2, 3, 4]
        self.solutionCase.partitionArray(A)
        result = A
        expect = [1,3,2,4]
        self.assertEqual(result, expect)
        
    def test_B(self):
        B = [1, 2, 1, 4]
        self.solutionCase.partitionArray(B)
        result = B
        expect = [1,1,2,4]
        self.assertEqual(result, expect)


class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        index_odd = 0
        for index in range(len(nums)):
            if nums[index] % 2:
                if index != index_odd:
                    nums[index], nums[index_odd] = nums[index_odd], nums[index]
                index_odd += 1


if __name__ == '__main__':
    unittest.main()
