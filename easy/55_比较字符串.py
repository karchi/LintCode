#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 55. 比较字符串,题目地址：https://www.lintcode.com/problem/compare-strings/description
# 比较两个字符串A和B，确定A中是否包含B中所有的字符。字符串A和B中的字符都是 大写字母
# 在 A 中出现的 B 字符串里的字符不需要连续或者有序。
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        A = "ABCD"
        B = "ACD"
        result = self.solutionCase.compareStrings(A, B)
        expect = True
        self.assertEqual(result, expect)
        
    def test_1(self):
        A = "ABCD"
        B = "AABC"
        result = self.solutionCase.compareStrings(A, B)
        expect = False
        self.assertEqual(result, expect)
        
    def test_2(self):
        A = "A"
        B = "AABC"
        result = self.solutionCase.compareStrings(A, B)
        expect = False
        self.assertEqual(result, expect)
        
    def test_3(self):
        A = "BA"
        B = "AABBA"
        result = self.solutionCase.compareStrings(A, B)
        expect = False
        self.assertEqual(result, expect)
    

class Solution:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    def compareStrings(self, A, B):
        res = True
        A = list(A)
        B = list(B)
        for item in B:
            if item not in A:
                res = False
                break
            A.remove(item)
        return res
        

if __name__ == '__main__':
    unittest.main()
