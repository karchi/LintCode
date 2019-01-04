#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 5. 第k大元素,题目地址：https://www.lintcode.com/problem/kth-largest-element/description
# 在数组中找到第k大的元素。你可以交换数组中的元素的位置。
# 样例:给出数组 [9,3,2,4,8]，第三大的元素是 4。给出数组 [1,2,3,4,5]，第一大的元素是 5，第二大的元素是 4，第三大的元素是 3，以此类推
# 挑战：要求时间复杂度为O(n)，空间复杂度为O(1)
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.kthLargestElement(3, [9,3,2,4,8])
        expect = 4
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.kthLargestElement(1, [1,2,3,4,5])
        expect =  5
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.kthLargestElement(2, [1,2,3,4,5])
        expect = 4
        self.assertEqual(result, expect)
        
    def test_3(self):
        result = self.solutionCase.kthLargestElement(3, [9,3,2,4,8])
        expect = 4
        self.assertEqual(result, expect)
    

# 解法一：
class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        return sorted(nums)[-n]


'''
# 解法二，超时：
class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        for i in nums:
            if len([j for j in nums if j>=i]) == n:
                return i
'''
        
        
if __name__ == '__main__':
    unittest.main()

