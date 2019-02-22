#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 1535. 转换成小写字母,题目地址：https://www.lintcode.com/problem/to-lower-case/description
# 实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。
# 样例:
# Example 1:Input: "Hello",Output: "hello"
# Example 2:Input: "here",Output: "here"
# Example 3:Input: "LOVELY",Output: "lovely"
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.toLowerCase("Hello")
        expect = "hello"
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.toLowerCase("here")
        expect =  "here"
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.toLowerCase("LOVELY")
        expect = "lovely"
        self.assertEqual(result, expect)
        
        
class Solution:
    """
    @param str: the input string
    @return: The lower case string
    """
    def toLowerCase(self, str):
        return str.lower()


if __name__ == '__main__':
    unittest.main()
