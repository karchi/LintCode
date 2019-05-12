#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 646. 第一个独特字符位置，题目地址：https://www.lintcode.com/problem/first-position-unique-character/description
# 给出一个字符串。找到字符串中第一个不重复的字符然后返回它的下标。如果不存在这样的字符，返回 -1。
# 样例:
# 样例 1:输入 : s = "lintcode"，输出 : 0
# 样例 2:输入 : s = "lovelintcode"，输出 : 2
'''


import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.firstUniqChar("lintcode")
        expect = 0
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.firstUniqChar("lovelintcode")
        expect = 2
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.firstUniqChar("aabbcc")
        expect = -1
        self.assertEqual(result, expect)
        
        
class Solution:
    """
    @param s: a string
    @return: it's index
    """
    def firstUniqChar(self, s):
        pos = [s.index(i) for i in set(s) if s.count(i) == 1]
        return min(pos) if pos else -1


if __name__ == '__main__':
    unittest.main()
