#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 936. 首字母大写，题目地址：https://www.lintcode.com/problem/capitalizes-the-first-letter/description
# 输入一个英文句子，将每个单词的第一个字母改成大写字母
# 这个句子可能并不是一个符合语法规则的句子。
# 句子长度小于等于100。
# 样例:
# 样例 1:输入: s =  "i want to get an accepted"，输出: "I Want To Get An Accepted"
# 样例 2:输入: s =  "i jidls    mdijf  i  lsidj  i p l   "，输出: "I Jidls    Mdijf  I  Lsidj  I P L   "
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.capitalizesFirst("i want to get an accepted")
        expect = "I Want To Get An Accepted"
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.capitalizesFirst("i jidls    mdijf  i  lsidj  i p l   ")
        expect = "I Jidls    Mdijf  I  Lsidj  I P L   "
        self.assertEqual(result, expect)
        
     
class Solution:
    """
    @param s: a string
    @return: a string after capitalizes the first letter
    """
    def capitalizesFirst(self, s):
        res = s[0].upper()
        for i in s[1:]:
            if res[-1]==" ":
                res += i.upper()
            else:
                res += i
        return res


if __name__ == '__main__':
    unittest.main()
