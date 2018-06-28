#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 888. Valid Word Square,题目地址：https://www.lintcode.com/problem/valid-word-square/description
# Given a sequence of words, check whether it forms a valid word square.
# A sequence of words forms a valid word square if the k^th row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).
# The number of words given is at least 1 and does not exceed 500.
# Word length will be at least 1 and does not exceed 500.
# Each word contains only lowercase English alphabet a-z.
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.validWordSquare(["abcd","bnrt","crmy","dtye"])
        expect = True
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.validWordSquare(["abcd","bnrt","crm","dt"])
        expect = True
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.validWordSquare(["ball","area","read","lady"])
        expect = False
        self.assertEqual(result, expect)
        
    def test_3(self):
        result = self.solutionCase.validWordSquare(["abcde","bbcd","cccde","ddd","e"])
        expect = False
        self.assertEqual(result, expect)
        
    def test_4(self):
        result = self.solutionCase.validWordSquare(["abcde","bbcd","cccde","ddd","ee"])
        expect = False
        self.assertEqual(result, expect)
    

class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        for i in range(len(words)):
            for j in range(len(words[i])):
                try:
                    if words[i][j] != words[j][i]:
                        return False
                except IndexError:
                    return False
        return True


if __name__ == '__main__':
    unittest.main()

