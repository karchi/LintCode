#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 766. 闰年,题目地址：https://www.lintcode.com/problem/leap-year/description
# 判断给出的年份 n 是否为闰年. 如果 n 为闰年则返回 true
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.isLeapYear(2008)
        expect = True
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.isLeapYear(2018)
        expect = False
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.isLeapYear(2000)
        expect = True
        self.assertEqual(result, expect)
        
    def test_3(self):
        result = self.solutionCase.isLeapYear(1000)
        expect = False
        self.assertEqual(result, expect)
    

# class Solution:
    # """
    # @param n: a number represent year
    # @return: whether year n is a leap year.
    # """
    # def isLeapYear(self, n):
        # res = False
        # if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
            # res = True
        # return res

class Solution:
    """
    @param n: a number represent year
    @return: whether year n is a leap year.
    """
    def isLeapYear(self, n):
        return True if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0 else False
        
        
if __name__ == '__main__':
    unittest.main()

