#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 1332. 判断一个整数中有多少个1，题目地址：https://www.lintcode.com/problem/number-of-1-bits/description
# 写一个函数，其以无符号整数为输入，而输出它所具有的“1”的位数（也被称为汉明权重）
# 样例:
# 样例 1:输入：n = 11,输出：3,解析：11(10) = 1011(2), 返回 3
# 样例 2:输入：n = 7,输出：3,解析：7(10) = 111(2), 返回 3
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.hammingWeight(11)
        expect = 3
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.hammingWeight(7)
        expect =  3
        self.assertEqual(result, expect)
        
        
class Solution:
    """
    @param n: an unsigned integer
    @return: the number of 1 bits
    """
    def hammingWeight(self, n):
        return bin(n)[2:].count("1")


if __name__ == '__main__':
    unittest.main()
