#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 765. 有效的三角形,题目地址：https://www.lintcode.com/problem/valid-triangle/description
# 给出三个整数 a, b, c, 如果它们可以构成三角形,返回 true.
# 样例:给定 a = 2, b = 3, c = 4，返回 true
# 给定 a = 1, b = 2, c = 3，返回 false
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.isValidTriangle(2,3,4)
        expect = True
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.isValidTriangle(1,2,3)
        expect =  False
        self.assertEqual(result, expect)
    

# 解法一：
class Solution:
    """
    @param a: a integer represent the length of one edge
    @param b: a integer represent the length of one edge
    @param c: a integer represent the length of one edge
    @return: whether three edges can form a triangle
    """
    def isValidTriangle(self, a, b, c):
        triangle = sorted([a,b,c])
        return triangle[0] + triangle[1] > triangle[2]

        
if __name__ == '__main__':
    unittest.main()
