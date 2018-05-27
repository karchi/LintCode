#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 463.整数排序,题目地址：https://www.lintcode.com/problem/sort-integers/description
# 给一组整数，按照升序排序，使用选择排序，冒泡排序，插入排序或者任何 O(n2) 的排序算法。
'''

import unittest
import random


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solution_case = Solution()
        
    def test1(self):
        A = [3, 2, 1, 4, 5]
        self.solution_case.sortIntegers(A)
        expect = [1, 2, 3, 4, 5]
        self.assertEqual(A, expect)
        
    def test_empty(self):
        A = []
        self.solution_case.sortIntegers(A)
        expect = []
        self.assertEqual(A, expect)
        
    def test_random_list(self):
        A = []
        B = []
        for times in range(1000):
            number = random.randint(0, 9999)
            A.append(number)
            B.append(number)
        self.solution_case.sortIntegers(A)
        B.sort()
        self.assertEqual(A, B)


'''
# 解法1：
class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers(self, A):
        A.sort()
'''


# 冒泡排序：
class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers(self, A):
        for i in range(len(A)):
            for j in range(len(A)-1, i, -1):
                if A[j-1] > A[j]:
                    A[j-1], A[j] = A[j], A[j-1]


if __name__ == '__main__':
    unittest.main()
