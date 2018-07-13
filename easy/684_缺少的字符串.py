#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 684. 缺少的字符串,题目地址：https://www.lintcode.com/problem/missing-string/description
# 给出两个字符串，你需要找到缺少的字符串
# 给一个字符串 str1 = "This is an example", 给出另一个字符串 str2 = "is example"
# 返回 ["This", "an"]
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.missingString("This is an example", "is example")
        expect = ["This", "an"]
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.missingString("is example", "is example")
        expect = []
        self.assertEqual(result, expect)
        

class Solution:
    """
    @param str1: a given string
    @param str2: another given string
    @return: An array of missing string
    """
    def missingString(self, str1, str2):
        return [strings for strings in str1.split() if strings not in str2.split()]


if __name__ == '__main__':
    unittest.main()

