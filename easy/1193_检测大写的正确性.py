#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 1193. 检测大写的正确性,题目地址：https://www.lintcode.com/problem/detect-capital/description
# Given a word, you need to judge whether the usage of capitals in it is right or not.We define the usage of capitals in a word to be right when one of the following cases holds:
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital if it has more than one letter, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.
# 输入将是一个由大写和小写拉丁字母组成的非空单词。
# 样例:
# Input: "USA",Output: True
# Input: "FlaG",Output: False
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.detectCapitalUse("USA")
        expect = True
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.detectCapitalUse("FlaG")
        expect =  False
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.detectCapitalUse("Google")
        expect = True
        self.assertEqual(result, expect)
        
    def test_3(self):
        result = self.solutionCase.detectCapitalUse("leetcode")
        expect = True
        self.assertEqual(result, expect)


class Solution:
    """
    @param word: a string
    @return: return a boolean
    """
    def detectCapitalUse(self, word):
        return word.isupper() or word[1:].islower()


if __name__ == '__main__':
    unittest.main()
