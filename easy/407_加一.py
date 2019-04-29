#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 407. 加一，题目地址：https://www.lintcode.com/problem/plus-one/description
# 给定一个非负数，表示一个数字数组，在该数的基础上+1，返回一个新的数组。
# 该数字按照数位高低进行排列，最高位的数在列表的最前面。
# 样例:
# 样例 1:输入：[1,2,3],输出：[1,2,4]
# 样例 2:输入：[9,9,9],输出：[1,0,0,0]
'''


import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.plusOne([1,2,3])
        expect = [1,2,4]
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.plusOne([9,9,9])
        expect = [1,0,0,0]
        self.assertEqual(result, expect)
        
        
'''
# 解法一：
class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        w = sum = 0
        while digits:
            sum += digits.pop(-1) * 10 ** w
            w += 1
        sum += 1
        res = []
        while sum:
            res.insert(0, sum % 10)
            sum = sum // 10
        return res
'''
    
   
# 解法二：
class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        sum = int("".join([str(i) for i in digits])) + 1
        res = [int(i) for i in str(sum)]
        return res


if __name__ == '__main__':
    unittest.main()
