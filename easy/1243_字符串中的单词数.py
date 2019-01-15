#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 1243. 字符串中的单词数,题目地址：https://www.lintcode.com/problem/number-of-segments-in-a-string/description
# 计算字符串中的单词数，其中一个单词定义为不含空格的连续字符串。
# 字符串中不包含任何 无法打印 的字符.
# 样例:输入: "Hello, my name is John",输出: 5
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.countSegments("Hello, my name is John")
        expect = 5
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.countSegments(" aaa hhh")
        expect =  2
        self.assertEqual(result, expect)
        

# 解法一：
class Solution:
    """
    @param s: a string
    @return: the number of segments in a string
    """
    def countSegments(self, s):
        return len([i for i in s.split(" ") if len(i) > 0 ])


if __name__ == '__main__':
    unittest.main()
