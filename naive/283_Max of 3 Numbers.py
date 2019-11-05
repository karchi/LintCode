#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 283. Max of 3 Numbers，题目地址：https://www.lintcode.com/problem/max-of-3-numbers/description
# 给三个整数，求他们中的最大值。
# 样例:
# 样例 1:输入:num1 = 1, num2 = 9, num3 = 0，输出: 9
# 样例 2:输入:num1 = 1, num2 = 2, num3 = 3，输出: 3
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.maxOfThreeNumbers(1, 9, 0)
        expect = 9
        self.assertEqual(result, expect)
    
    def test_1(self):
        result = self.solutionCase.maxOfThreeNumbers(1, 2, 3)
        expect = 3
        self.assertEqual(result, expect)
        

class Solution:
    """
    @param num1: An integer
    @param num2: An integer
    @param num3: An integer
    @return: an interger
    """
    def maxOfThreeNumbers(self, num1, num2, num3):
        return max(num1, num2, num3)


if __name__ == '__main__':
    unittest.main()
