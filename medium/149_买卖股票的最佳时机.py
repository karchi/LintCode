#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 买卖股票的最佳时机,题目地址：https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock/description
假设有一个数组，它的第i个元素是一支给定的股票在第i天的价格。如果你最多只允许完成一次交易(例如,一次买卖股票),设计一个算法来找出最大利润。
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_explame(self):
        self.assertEqual(self.solutionCase.maxProfit([3,2,3,1,2]), 1)
        
    def test_empty(self):
        self.assertEqual(self.solutionCase.maxProfit([]), 0)
        
    def test_low(self):
        self.assertEqual(self.solutionCase.maxProfit([2,1]), 0)
        
    def test_high(self):
        self.assertEqual(self.solutionCase.maxProfit([1,2]), 1)
        

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        res = 0
        if prices:
            buyPoint = prices[0]
            sellPoint = prices[0]
        for i in prices:
            if i > sellPoint:
                sellPoint = i
                res = max(sellPoint - buyPoint, res)
            elif i < buyPoint:
                buyPoint = i
                sellPoint = i
        return res
        

if __name__ == '__main__':
    unittest.main()


