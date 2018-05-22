#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 394. 硬币排成线,题目地址：https://www.lintcode.com/problem/coins-in-a-line/description
# 有 n 个硬币排成一条线。两个参赛者轮流从右边依次拿走 1 或 2 个硬币，直到没有硬币为止。拿到最后一枚硬币的人获胜。
# 请判定 第一个玩家 是输还是赢？
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solution_case = Solution()
        
    def test1(self):
        self.assertEqual(self.solution_case.firstWillWin(1), True)
        
    def test2(self):
        self.assertEqual(self.solution_case.firstWillWin(2), True)
        
    def test3(self):
        self.assertEqual(self.solution_case.firstWillWin(3), False)
        
    def test4(self):
        self.assertEqual(self.solution_case.firstWillWin(6), False)
        
    def test5(self):
        self.assertEqual(self.solution_case.firstWillWin(100), True)
        

class Solution:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        return n % 3 != 0
        
    
if __name__ == '__main__':
    unittest.main()


