#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 114. 不同的路径，题目地址：https://www.lintcode.com/problem/unique-paths/description
# 有一个机器人的位于一个 m × n 个网格左上角。机器人每一时刻只能向下或者向右移动一步。机器人试图达到网格的右下角。问有多少条不同的路径？
# n和m均不超过100
# 样例:
# 样例 1:Input: n = 1, m = 3; Output: 1; Explanation: Only one path to target position.
# 样例 2:输入: Input:  n = 3, m = 3; Output: 6; Explanation:
	# D : Down
	# R : Right
	# 1) DDRR
	# 2) DRDR
	# 3) DRRD
	# 4) RRDD
	# 5) RDRD
	# 6) RDDR
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.uniquePaths(3, 1)
        expect = 1
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.uniquePaths(3, 3)
        expect = 6
        self.assertEqual(result, expect)
        
    def test_2(self):
        result = self.solutionCase.uniquePaths(10, 10)
        expect = 48620
        self.assertEqual(result, expect)

    def test_3(self):
        result = self.solutionCase.uniquePaths(4, 5)
        expect = 35
        self.assertEqual(result, expect)
        
    def test_4(self):
        result = self.solutionCase.uniquePaths(1, 1)
        expect = 1
        self.assertEqual(result, expect)


# 解法一：递归(超时)
'''
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        else:
            return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
'''


# 解法二：动态规划
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        dp = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


if __name__ == '__main__':
    unittest.main()
