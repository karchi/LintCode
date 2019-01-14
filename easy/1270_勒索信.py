#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 1270. 勒索信,题目地址：hhttps://www.lintcode.com/problem/ransom-note/description
# 给定一个任意的表示勒索信内容的字符串，和另一个字符串，表示能从杂志中获取到的所有字符，写一个方法判断能否通过剪下杂志中的字符来构造出这封勒索信，若可以，返回 true；否则返回 false。
# 杂志字符串中的每一个字符仅能在勒索信中使用一次。
# 你可以认为两个字符串都只包含小写字母。
# 样例:canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.canConstruct("a", "b")
        expect = False
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.canConstruct("aa", "ab")
        expect =  False
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.canConstruct("aa", "aab")
        expect = True
        self.assertEqual(result, expect)
        
   
# 解法一：
class Solution:
    """
    @param ransomNote: a string
    @param magazine: a string
    @return: whether the ransom note can be constructed from the magazines
    """
    def canConstruct(self, ransomNote, magazine):
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        while ransomNote:
            if ransomNote[0] in magazine:
                magazine.remove(ransomNote[0])
                ransomNote.pop(0)
            else:
                return False
        return True

        
if __name__ == '__main__':
    unittest.main()
