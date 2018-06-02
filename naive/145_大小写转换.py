#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 145. 大小写转换,题目地址：https://www.lintcode.com/problem/lowercase-to-uppercase/description
# 将一个字符由小写字母转换为大写字母
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_a(self):
        result = self.solutionCase.lowercaseToUppercase("a")
        expect = "A"
        self.assertEqual(result, expect)
        
    def test_b(self):
        result = self.solutionCase.lowercaseToUppercase("b")
        expect = "B"
        self.assertEqual(result, expect)
        
    def test_z(self):
        result = self.solutionCase.lowercaseToUppercase("z")
        expect = "Z"
        self.assertEqual(result, expect)
    

class Solution:
    """
    @param character: a character
    @return: a character
    """
    def lowercaseToUppercase(self, character):
        return character.upper()


if __name__ == '__main__':
    unittest.main()

