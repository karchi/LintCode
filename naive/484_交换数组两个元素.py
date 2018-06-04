#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 484. 交换数组两个元素,题目地址：https://www.lintcode.com/problem/swap-two-integers-in-array/description
# 给你一个数组和两个索引，交换下标为这两个索引的数字
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_1234(self):
        A = [1,2,3,4]
        self.solutionCase.swapIntegers(A, 2, 3)
        expect = [1,2,4,3]
        self.assertEqual(A, expect)
        
    def test_12(self):
        A = [1,2]
        self.solutionCase.swapIntegers(A, 1, 0)
        expect = [2,1]
        self.assertEqual(A, expect)
        
    
class Solution:
    """
    @param A: An integer array
    @param index1: the first index
    @param index2: the second index
    @return: nothing
    """
    def swapIntegers(self, A, index1, index2):
        A[index1], A[index2] = A[index2], A[index1]


if __name__ == '__main__':
    unittest.main()

