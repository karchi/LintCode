#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 2. 尾部的零,题目地址：https://www.lintcode.com/problem/trailing-zeros/description
# 设计一个算法，计算出n阶乘中尾部零的个数
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_1(self):
        result = self.solutionCase.trailingZeros(1)
        expect = 0
        self.assertEqual(result, expect)
        
    def test_0(self):
        result = self.solutionCase.trailingZeros(0)
        expect = 0
        self.assertEqual(result, expect)
        
    def test_11(self):
        result = self.solutionCase.trailingZeros(11)
        expect = 2
        self.assertEqual(result, expect)
        
    def test_1001171717(self):
        result = self.solutionCase.trailingZeros(1001171717)
        expect = 250292920
        self.assertEqual(result, expect)


'''
# 解法1：超时
class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        result = 0
        if n > 0:
            for i in range(1, n+1):
                while i % 5 == 0:
                    result += 1
                    i /= 5
        return result
'''        
        
# 解法2：
class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        result = 0
        exponent = 1
        while 5 ** exponent <= n:
            result += (n // 5 ** exponent)
            exponent += 1
        return result      

        
if __name__ == '__main__':
    unittest.main()



