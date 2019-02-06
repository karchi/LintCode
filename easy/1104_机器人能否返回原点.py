#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 1104. 机器人能否返回原点,题目地址：https://www.lintcode.com/problem/judge-route-circle/description
# 最初，机器人位于(0, 0)处。 给定一系列动作，判断该机器人的移动轨迹是否是一个环，这意味着它最终会回到原来的位置。移动的顺序由字符串表示。 每个动作都由一个字符表示。 有效的机器人移动是R（右），L（左），U（上）和D（下）。 输出应该为true或false，表示机器人是否回到原点。
# 样例:
# 样例1:输入: "UD"，输出: true
# 样例2:输入: "LL"，输出: false
'''


import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.judgeCircle("UD")
        expect = True
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.judgeCircle("LL")
        expect =  False
        self.assertEqual(result, expect)

        
class Solution:
    """
    @param moves: a sequence of its moves
    @return: if this robot makes a circle
    """
    def judgeCircle(self, moves):
        moves = list(moves)
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")


if __name__ == '__main__':
    unittest.main()
