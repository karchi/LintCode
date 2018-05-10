#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 落单的数,题目地址：https://www.lintcode.com/problem/single-number/description
给出2*n + 1 个的数字，除其中一个数字之外其他每个数字均出现两次，找到这个数字。
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_7(self):
        self.assertEqual(self.solutionCase.singleNumber([1,2,2,1,3,4,3]), 4)
        
    def test_empty(self):
        self.assertEqual(self.solutionCase.singleNumber([]), 0)


class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        res = 0
        if A != []:
            setA = set(A)
            for number in setA:
                if A.count(number) == 1:
                    res = number
                    break
        return res

    
if __name__ == '__main__':
    unittest.main()
