#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 422. 最后一个单词的长度，题目地址：https://www.lintcode.com/problem/length-of-last-word/description
# 给定一个字符串， 包含大小写字母、空格 ' '，请返回其最后一个单词的长度。
# 如果不存在最后一个单词，请返回 0 。
# 一个单词的界定是，由字母组成，但不包含任何的空格。
# 样例:
# 样例 1:输入："Hello World",输出：5
# 样例 2:输入："Hello LintCode",输出：8
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.lengthOfLastWord("Hello World")
        expect = 5
        self.assertEqual(result, expect)
    
    def test_1(self):
        result = self.solutionCase.lengthOfLastWord("Hello and hi LintCode")
        expect = 8
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.lengthOfLastWord("")
        expect = 0
        self.assertEqual(result, expect)

    def test_3(self):
        result = self.solutionCase.lengthOfLastWord("b a ")
        expect = 1
        self.assertEqual(result, expect)
        
        
class Solution:
    """
    @param s: A string
    @return: the length of last word
    """
    def lengthOfLastWord(self, s):
        return [len(i) for i in s.split(" ") if i][-1] if s else 0


if __name__ == '__main__':
    unittest.main()
