#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 判断字符串是否没有重复字符,题目地址：https://www.lintcode.com/problem/unique-characters/description
实现一个算法确定字符串中的字符是否均唯一出现
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_abc(self):
        self.assertEqual(self.solutionCase.isUnique("abc"), True)
        
    def test_aab(self):
        self.assertEqual(self.solutionCase.isUnique("aab"), False)


class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):
        return len(str) == len(set(str))

    
if __name__ == '__main__':
    unittest.main()

