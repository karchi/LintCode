#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 916. 回文排列,题目地址：https://www.lintcode.com/problem/palindrome-permutation/description
# 给定一个字符串，判断字符串是否存在一个排列是回文排列。
# 样例:
# 样例1:输入: s = "code",输出: False,解释:没有合法的回文排列
# 样例2:输入: s = "aab",输出: True,解释:"aab" --> "aba"
# 样例3:输入: s = "carerac",输出: True,解释:"carerac" --> "carerac"
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.canPermutePalindrome("code")
        expect = False
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.canPermutePalindrome("aab")
        expect =  True
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.canPermutePalindrome("carerac")
        expect = True
        self.assertEqual(result, expect)
        
    def test_3(self):
        result = self.solutionCase.canPermutePalindrome("aabbhijkbbhijkbbhijkkjihijkkjihijkkjihijkkjih")
        expect = True
        self.assertEqual(result, expect)
        
        
class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        odd = []
        res = True
        for string in s:
            if s.count(string) % 2 == 1 and string not in odd:
                odd.append(string)
            if len(odd) > 1:
                res = False
                break
        return res


if __name__ == '__main__':
    unittest.main()