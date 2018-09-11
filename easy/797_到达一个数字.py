#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 797. 到达一个数字,题目地址：https://www.lintcode.com/problem/reach-a-number/description
# 你站在一个无穷数轴上的 0 位置。在位置目标上有一个目标。
# 在每一个动作中，你可以向左或向右。在第n次移动中(从1开始)，你行走n步。
# 返回到达目的地所需的最小步骤数。
# 目标将是一个非零的整数范围[-10^9, 10^9]。
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.reachNumber(3)
        expect = 2
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.reachNumber(2)
        expect = 3
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.reachNumber(-2)
        expect = 3
        self.assertEqual(result, expect)
        
    def test_3(self):
        result = self.solutionCase.reachNumber(5)
        expect = 5
        self.assertEqual(result, expect)
    

class Solution:
    """
    @param target: the destination
    @return: the minimum number of steps
    """
    def reachNumber(self, target):
        target = abs(target)
        sum = 0
        n = 0
        res = n
        while sum < target:
            n +=1
            sum += n
        if (sum - target) % 2 == 0:
            res = n
        else:
            if n % 2 == 0:
                res = n+1
            else:
                res = n+2
        return res


if __name__ == '__main__':
    unittest.main()

