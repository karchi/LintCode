#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 1285. 四的乘方，题目地址：https://www.lintcode.com/problem/power-of-four/description
# 给定一个整数（32位有符号整数），写一个方法判断这个数字是否为4的乘方。
# 假设一个正整数的二进制表示不包含前导零。
# 样例:
# 样例 1:输入：num = 16,输出：True
# 样例 2:输入：num = 5,输出：False
# 挑战:你能否不使用循环/递归解决这个问题呢？
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.isPowerOfFour(16)
        expect = True
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.isPowerOfFour(5)
        expect =  False
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.isPowerOfFour(1)
        expect = True
        self.assertEqual(result, expect)
        
        
'''
# 解法一：
class Solution:
    """
    @param num: an integer
    @return: whether the integer is a power of 4
    """
    def isPowerOfFour(self, num):
        res = False
        s = 0
        while 4**s < num:
            s += 1
        if 4**s == num:
            res = True
        return res
'''


# 解法二，不使用循环或递归：
class Solution:
    """
    @param num: an integer
    @return: whether the integer is a power of 4
    """
    def isPowerOfFour(self, num):
        return (num & (num - 1) == 0) and ((num & 0x55555555) != 0)


if __name__ == '__main__':
    unittest.main()
