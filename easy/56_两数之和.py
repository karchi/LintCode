#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 56. 两数之和,题目地址：https://www.lintcode.com/problem/two-sum/
# 给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。你需要实现的函数twoSum需要返回这两个数的下标, 并且第一个下标小于第二个下标。注意这里下标的范围是 0 到 n-1。你可以假设只有一组答案。
# 样例:给出 numbers = [2, 7, 11, 15], target = 9, 返回 [0, 1].
# 挑战:Either of the following solutions are acceptable:
# O(n) Space, O(nlogn) Time
# O(n) Space, O(n) Time
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.twoSum([2, 7, 11, 15],9)
        expect = [0, 1]
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.twoSum([2, 7, 11, 15],18)
        expect = [1, 2]
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.twoSum([2, 7, 11, 15],26)
        expect = [2, 3]
        self.assertEqual(result, expect)
        
    def test_3(self):
        result = self.solutionCase.twoSum([0,4,3,0],0)
        expect = [0,3]
        self.assertEqual(result, expect)
    

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        for i in range(len(numbers)-1):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    return [i, j]


if __name__ == '__main__':
    unittest.main()

