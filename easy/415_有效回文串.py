#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 415. 有效回文串,题目地址：https://www.lintcode.com/problem/valid-palindrome/description
# 给定一个字符串，判断其是否为一个回文串。只考虑字母和数字，忽略大小写。
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.isPalindrome("A man, a plan, a canal: Panama")
        expect = True
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.isPalindrome("race a car")
        expect = False
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.isPalindrome("")
        expect = True
        self.assertEqual(result, expect)
    

class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        import re
        pattern = re.compile(r'[a-zA-Z0-9]+')
        text = list("".join(re.findall(pattern, s)).lower())
        return True if text == text[::-1] else False


if __name__ == '__main__':
    unittest.main()

