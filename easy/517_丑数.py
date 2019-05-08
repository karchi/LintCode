#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 517. 丑数，题目地址：https://www.lintcode.com/problem/ugly-number/description
# 写一个程序来检测一个整数是不是丑数。
# 丑数的定义是，只包含质因子 2, 3, 5 的正整数。比如 6, 8 就是丑数，但是 14 不是丑数因为他包含了质因子 7。
# 可以认为 1 是一个特殊的丑数。
# 样例:
# 样例 1:输入: num = 8，输出: true，解释:8=2*2*2
# 样例 2:输入: num = 14，输出: false，解释:14=2*7 
'''


import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.isUgly(8)
        expect = True
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.isUgly(14)
        expect = False
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.isUgly(0)
        expect = False
        self.assertEqual(result, expect)

        
class Solution:
    """
    @param num: An integer
    @return: true if num is an ugly number or false
    """
    def isUgly(self, num):
        while num > 5 and num % 2 == 0:
            num /= 2
        while num > 5 and num % 3 == 0:
            num /= 3
        while num > 5 and num % 5 == 0:
            num /= 5
        return True if 0 < num < 6 else False


if __name__ == '__main__':
    unittest.main()
