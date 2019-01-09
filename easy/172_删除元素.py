#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 172. 删除元素,题目地址：https://www.lintcode.com/problem/remove-element/description
# 给定一个数组和一个值，在原地删除与值相同的数字，返回新数组的长度。
# 元素的顺序可以改变，并且对新的数组不会有影响。
# 样例:给出一个数组 [0,4,4,0,0,2,4,4]，和值 4。返回 4 并且4个元素的新数组为[0,0,0,2]
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.removeElement([], 0)
        expect = 0
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.removeElement( [0,4,4,0,0,2,4,4], 4)
        expect =  4
        self.assertEqual(result, expect)
    

# 解法一：
class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        for i in A[:]:
            if i == elem:
                A.remove(i)
        return len(A)

        
if __name__ == '__main__':
    unittest.main()
