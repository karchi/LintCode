#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 209. 第一个只出现一次的字符，题目地址：https://www.lintcode.com/problem/first-unique-character-in-a-string/description
# 给出一个字符串，找出第一个只出现一次的字符。
# 样例:
# 样例 1:输入: "abaccdeff"，输出:  'b'，解释:'b' 是第一个出现一次的字符
# 样例 2:	输入: "aabccd"，输出:  'b'，解释:'b' 是第一个出现一次的字符
# 挑战：不使用额外的存储空间。
'''


import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.firstUniqChar("abaccdeff")
        expect = 'b'
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.firstUniqChar("aabccd")
        expect = 'b'
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.firstUniqChar("abbcddc")
        expect = 'a'
        self.assertEqual(result, expect)


class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        return str[min([str.index(i) for i in set(str) if str.count(i) == 1])]


if __name__ == '__main__':
    unittest.main()
