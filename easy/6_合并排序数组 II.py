#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 6. 合并排序数组 II,题目地址：https://www.lintcode.com/problem/merge-two-sorted-arrays/description
# 合并两个排序的整数数组A和B变成一个新的数组。
# 样例:给出A=[1,2,3,4]，B=[2,4,5,6]，返回 [1,2,2,3,4,4,5,6]
# 挑战:你能否优化你的算法，如果其中一个数组很大而另一个数组很小？
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.mergeSortedArray([1],[1])
        expect = [1,1]
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.mergeSortedArray([1,2,3,4],[2,4,5,6])
        expect =  [1,2,2,3,4,4,5,6]
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.mergeSortedArray([987,988,999],[1,5,1000])
        expect = [1,5,987,988,999,1000]
        self.assertEqual(result, expect)
        
    def test_3(self):
        result = self.solutionCase.mergeSortedArray([1,2,999],[5])
        expect = [1,2,5,999]
        self.assertEqual(result, expect)
    

# 解法一：
class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        return sorted(A+B)


'''
# 解法二：                
class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        result = []
        while A or B:
            if A == []:
                result.extend(B)
                break
            elif B == []:
                result.extend(A)
                break
            elif A[0]>=B[0]:
                result.append(B.pop(0))
            else:
                result.append(A.pop(0))
        return result
'''

if __name__ == '__main__':
    unittest.main()

