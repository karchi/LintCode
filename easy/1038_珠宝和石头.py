#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 1038. 珠宝和石头,题目地址：https://www.lintcode.com/problem/jewels-and-stones/description
# 给定字符串J代表是珠宝的石头类型，而S代表你拥有的石头.S中的每个字符都是你拥有的一个石头. 你想知道你的石头有多少是珠宝.
# J中的字母一定不同，J和S中的字符都是字母。 字母区分大小写，因此"a"和"A"是不同的类型.
# S和J由字母组成且长度最大为50.
# J中字符各不相同.
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.numJewelsInStones("aA", "aAAbbbb")
        expect = 3
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.numJewelsInStones("z", "ZZ")
        expect = 0
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.numJewelsInStones("", "ZZ")
        expect = 0
        self.assertEqual(result, expect)
        
    def test_3(self):
        result = self.solutionCase.numJewelsInStones("aB", "")
        expect = 0
        self.assertEqual(result, expect)
    

class Solution:
    """
    @param J: the types of stones that are jewels
    @param S: representing the stones you have
    @return: how many of the stones you have are also jewels
    """
    def numJewelsInStones(self, J, S):
        return sum([S.count(i) for i in J])


if __name__ == '__main__':
    unittest.main()

