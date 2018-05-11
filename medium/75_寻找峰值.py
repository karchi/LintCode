#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 寻找峰值 ,题目地址：https://www.lintcode.com/problem/find-peak-element/description
你给出一个整数数组(size为n)，其具有以下特点：
*相邻位置的数字是不同的
*A[0] < A[1] 并且 A[n - 2] > A[n - 1]
假定P是峰值的位置则满足A[P] > A[P-1]且A[P] > A[P+1]，返回数组中任意一个峰值的位置。
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solution_case = Solution()
        
    def test_8(self):
        input_example = [1,2,1,3,4,5,7,6]
        expect = [1, 6]
        result = self.solution_case.findPeak(input_example)
        self.assertTrue(result in expect)
        
    def test_longList(self):
        input_example = list(range(999998))
        input_example.append(1)
        expect = 999997
        result = self.solution_case.findPeak(input_example)
        self.assertEqual(result, expect)


'''
# Solution 1:顺序查找
class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        for i in range(1, len(A) - 1):
            if A[i - 1] < A[i] and A[i] > A[i + 1]:
                res = i
                break
        return res
'''

# Solution 2:二分查找
class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        start = 0
        end = len(A)
        mid = end // 2
        while mid:
            if A[mid-1]<A[mid] and A[mid]>A[mid+1]:
                break
            elif A[mid-1]<A[mid]:
                start = mid
                mid = (start + end) // 2
            else:
                end = mid
                mid = (start + end) // 2
        return mid


if __name__ == '__main__':
    unittest.main()


