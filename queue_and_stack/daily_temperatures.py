"""
739	 Daily Temperatures

Given a list of daily temperatures T, return a list such that,
for each day in the input, tells you how many days you would 
ave to wait until a warmer temperature. If there is no future day 
for which this is possible, put 0 instead.

For example, given the list of temperatures 
T = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100]. 

>>> solution = Solution()
>>> solution.dailyTemperatures([9, 8, 7, 6, 5, 4, 3, 2])
[0, 0, 0, 0, 0, 0, 0, 0]
>>> solution.dailyTemperatures([1, 1, 1, 2, 1, 1, 1, 1])
[3, 2, 1, 0, 0, 0, 0, 0]
>>> solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
[1, 1, 4, 2, 1, 1, 0, 0]
"""
from typing import List
class Solution:

    # def dailyTemperatures(self, T: List[int]) -> List[int]:
    #     """
    #     Brute-force solution in O(N^2) time
    #     """
    #     if not T:
    #         return []
    #     res = [0] * len(T)
    #     for i in range(len(T)):
    #         count = 1
    #         for j in range(i + 1, len(T)):
    #             if T[j] > T[i]:
    #                 res[i] = count
    #                 break
    #             else:
    #                 count += 1
    #     return res

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        Stack based solution. O(N)
        """
        if not T:
            return []
        res = [0] * len(T)
        stack = []
        for i in range(len(T)):
            cur = T[i]
            while stack and cur > stack[-1][0]:
                v = stack.pop()
                res[v[1]] = i - v[1]
            stack.append((cur, i))
        return res

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)