#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 993. 数组划分 I,题目地址：https://www.lintcode.com/problem/array-partition-i/description
# 给一个有 2n 个整数的数组，你的任务是把这些整数分成 n 组，如(a1, b1)，(a2, b2)，...，(an, bn)。并且使得 i 从 1 到 n 的 min(ai, bi)之和尽可能的大。
# 1. n 是一个正整数，且范围为 [1, 10000].
# 2. 数组中的元素范围为[-10000, 10000]。
# 样例:
# 样例1:输入: [1,4,3,2],输出: 4,解释: n 是 2, 最大的数对和为 4 = min(1, 2) + min(3, 4).
# 样例2:输入: [5,6],输出: 5,解释: n 是 1, 最大的数对和为 5 = min(5, 6).
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.arrayPairSum([1,4,3,2])
        expect = 4
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.arrayPairSum([5,6])
        expect =  5
        self.assertEqual(result, expect)

        
class Solution:
    """
    @param nums: an array
    @return: the sum of min(ai, bi) for all i from 1 to n
    """
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])


if __name__ == '__main__':
    unittest.main()
