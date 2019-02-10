#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 846. 多关键字排序,题目地址：https://www.lintcode.com/problem/multi-keyword-sort/description
# 给定 n 个学生的学号(从 1 到 n 编号)以及他们的考试成绩，表示为(学号，考试成绩)，请将这些学生按考试成绩降序排序，若考试成绩相同，则按学号升序排序。
# 样例:
# 输入: array = [[2,50],[1,50],[3,100]],输出: [[3,100],[1,50],[2,50]]
# 输入: array = [[2,50],[1,50],[3,50]],输出: [[1,50],[2,50],[3,50]]
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.multiSort([[2,50],[1,50],[3,100]])
        expect = [[3,100],[1,50],[2,50]]
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.multiSort([[2,50],[1,50],[3,50]])
        expect =  [[1,50],[2,50],[3,50]]
        self.assertEqual(result, expect)
        
        
class Solution:
    """
    @param array: the input array
    @return: the sorted array
    """
    def multiSort(self, array):
        return sorted(array, key=lambda x:[-x[1], x[0]])


if __name__ == '__main__':
    unittest.main()
