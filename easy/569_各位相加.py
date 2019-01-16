#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 569. 各位相加,题目地址：https://www.lintcode.com/problem/add-digits/description
# 给出一个非负整数 num，反复的将所有位上的数字相加，直到得到一个一位的整数。
# 样例:给出 num = 38。相加的过程如下：3 + 8 = 11，1 + 1 = 2。因为 2 只剩下一个数字，所以返回 2。
# 挑战：你可以不用任何的循环或者递归算法，在 O(1) 的时间内解决这个问题么？
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.addDigits(38)
        expect = 2
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.addDigits(9)
        expect =  9
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.addDigits(0)
        expect = 0
        self.assertEqual(result, expect)
        

# 解法一：
class Solution:
    """
    @param num: a non-negative integer
    @return: one digit
    """
    def addDigits(self, num):
        return num % 9 if num % 9 != 0 or num == 0 else 9



if __name__ == '__main__':
    unittest.main()
