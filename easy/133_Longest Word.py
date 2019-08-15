#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 133. Longest Word，题目地址：https://www.lintcode.com/problem/longest-word/description
# Given a dictionary, find all of the longest words in the dictionary.
# 样例:
# Example 1:Input: {"dog",	"google","facebook","internationalization","blabla"}
Output: ["internationalization"]
# Example 2:Input:  {"like","love","hate",	"yes"}
Output: ["like", "love", "hate"]
# Challenge：It's easy to solve it in two passes, can you do it in one pass?
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.longestWords(["dog","google","facebook","internationalization","blabla"])
        expect = ["internationalization"]
        self.assertEqual(result, expect)
    
    def test_1(self):
        result = self.solutionCase.longestWords(["like","love","hate","yes"])
        expect = ["like", "love", "hate"]
        self.assertEqual(result, expect)


# 解法一：
class Solution:
    """
    @param: dictionary: an array of strings
    @return: an arraylist of strings
    """
    def longestWords(self, dictionary):
        res =[]
        length = 0
        for i in dictionary:
            if len(i) > length:
                res = [i]
                length = len(i)
            elif len(i) == length:
                res.append(i)
        return res


# 解法二：Time Limit Exceeded
# class Solution:
#     """
#     @param: dictionary: an array of strings
#     @return: an arraylist of strings
#     """
#     def longestWords(self, dictionary):
#         return [i for i in dictionary if len(i)==max([len(i)for i in dictionary])]


if __name__ == '__main__':
    unittest.main()
