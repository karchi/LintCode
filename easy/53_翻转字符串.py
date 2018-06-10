#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 53. 翻转字符串,题目地址：https://www.lintcode.com/problem/reverse-words-in-a-string/description
# 给定一个字符串，逐个翻转字符串中的每个单词。
# 单词的构成：无空格字母构成一个单词
# 输入字符串是否包括前导或者尾随空格？可以包括，但是反转后的字符不能包括
# 如何处理两个单词间的多个空格？在反转字符串中间空格减少到只含一个
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.reverseWords("")
        expect = ""
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.reverseWords(" abc  ddefc cxoe coacgo  ")
        expect = "coacgo cxoe ddefc abc"
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.reverseWords("  abc  ")
        expect = "abc"
        self.assertEqual(result, expect)
    

class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])


if __name__ == '__main__':
    unittest.main()

