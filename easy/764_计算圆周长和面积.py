#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 764. 计算圆周长和面积,题目地址：https://www.lintcode.com/problem/calculate-circumference-and-area/description
# 给定半径r，返回圆的周长nums[0]和面积nums[1].结果保留了两位小数.
# PI = 3.14
# 样例:
# 给定 r = 2，return [12.56, 12.56]
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.calculate(2)
        expect = [12.56, 12.56]
        self.assertEqual(result, expect)
        
        
class Solution:
    """
    @param r: a Integer represent radius
    @return: the circle's circumference nums[0] and area nums[1]
    """
    def calculate(self, r):
        PI = 3.14
        return [2*PI*r, r**2*PI]


if __name__ == '__main__':
    unittest.main()
