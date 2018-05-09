#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# Fizz Buzz 问题,题目地址：https://www.lintcode.com/problem/fizz-buzz/description
给你一个整数n. 从 1 到 n 按照下面的规则打印每个数：

*如果这个数被3整除，打印fizz.
*如果这个数被5整除，打印buzz.
*如果这个数能同时被3和5整除，打印fizz buzz.
'''

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
    def test_15(self):
        solution = Solution()
        expect = [
                "1", "2", "fizz","4", "buzz", "fizz","7", "8", "fizz","buzz",
                "11", "fizz","13","14", "fizz buzz"
                ]
        result = solution.fizzBuzz(15)
        self.assertEqual(expect, result)
    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.fizzBuzz(1), ["1"])
    def test_7(self):
        solution = Solution()
        self.assertEqual(solution.fizzBuzz(7), ["1", "2", "fizz", "4", "buzz", "fizz", "7"])


class Solution:
    """
    @param n: An integer as description
    @return: A list of strings.
    For example, if n = 7, your code should return
        ["1", "2", "fizz", "4", "buzz", "fizz", "7"]
    """
    def fizzBuzz(self, n):
        results = []
        for i in range(1, n+1):
            if i % 15 == 0:
                results.append("fizz buzz")
            elif i % 5 == 0:
                results.append("buzz")
            elif i % 3 == 0:
                results.append("fizz")
            else:
                results.append(str(i))
        return results

    
if __name__ == '__main__':
    unittest.main()