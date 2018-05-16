#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 366.斐波纳契数列,题目地址：https://www.lintcode.com/problem/fibonacci/
查找斐波纳契数列中第 N 个数。
所谓的斐波纳契数列是指：
* 前2个数是 0 和 1 。
* 第 i 个数是第 i-1 个数和第i-2 个数的和。
斐波纳契数列的前10个数字是：
0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test1(self):
        self.assertEqual(self.solutionCase.fibonacci(1), 0)
        
    def test2(self):
        self.assertEqual(self.solutionCase.fibonacci(2), 1)
        
    def test3(self):
        self.assertEqual(self.solutionCase.fibonacci(10), 34)


class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        if n == 1:
            res = 0
        elif n == 2:
            res = 1
        else:
            a = 0
            res = 1
            for i in range(2, n):
                a, res = res, a + res
        return res

    
if __name__ == '__main__':
    unittest.main()

