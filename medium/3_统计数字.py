#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 3. 统计数字,题目地址：https://www.lintcode.com/problem/digit-counts/description
# 计算数字k在0到n中的出现的次数，k可能是0~9的一个值
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0_0(self):
        result = self.solutionCase.digitCounts(0, 0)
        expect = 1
        self.assertEqual(result, expect)
        
    def test_5_3(self):
        result = self.solutionCase.digitCounts(5, 3)
        expect = 0
        self.assertEqual(result, expect)
        
    def test_1_12(self):
        result = self.solutionCase.digitCounts(1, 12)
        expect = 5
        self.assertEqual(result, expect)
    

class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digitCounts(self, k, n):
        numbers = list(range(n+1))
        strings = ""
        for number in numbers:
            strings += str(number)
        return strings.count(str(k))


if __name__ == '__main__':
    unittest.main()

