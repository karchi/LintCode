#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 1252. 根据身高重排队列,题目地址：https://www.lintcode.com/problem/queue-reconstruction-by-height/description
# 假设你有一个顺序被随机打乱的列表，代表了站成一列的人群。每个人被表示成一个二元组(h, k)，其中h表示他的身高，k表示站在他之前的身高高于或等于h的人数。你需要将这个队列重新排列以恢复其原有的顺序。
# 总人数小于1,100。
# 样例:
# 输入：[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# 输出：[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''

import unittest


class TestCases(unittest.TestCase):
    def setUp(self):
        self.solutionCase = Solution()
        
    def test_0(self):
        result = self.solutionCase.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
        expect = [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
        self.assertEqual(result, expect)
        
    def test_1(self):
        result = self.solutionCase.reconstructQueue([[1,0]])
        expect =  [[1,0]]
        self.assertEqual(result, expect)
        

class Solution:
    """
    @param people: a random list of people
    @return: the queue that be reconstructed
    """
    def reconstructQueue(self, people):
        people = sorted(people, key = lambda x:(-x[0], x[1]))
        res = []
        for i in people:
            if i[1] == i:
                res.append([i])
            else:
                res.insert(i[1], i)
        return res

        
if __name__ == '__main__':
    unittest.main()
