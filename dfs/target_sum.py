"""
494. Target Sum
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S.
Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

>>> solution = Solution()
>>> solution.findTargetSumWays([1, 1, 1, 1, 1], 3)
5
>>> solution.findTargetSumWays([42,36,4,15,17,15,31,1,11,2,12,28,22,9,2,31,48,18,48,5], 15)
7219
"""
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        memo = {}
        def dfs(start, end, cur):
            pair = (start, cur)
            if pair in memo:
                return memo[pair]
            if start == end:
                if cur == S:
                    return 1
                else:
                    return 0
            val = dfs(start + 1, end, cur + nums[start]) + \
                    dfs(start + 1, end, cur - nums[start])
            memo[pair] = val
            return val
        
        return dfs(0, len(nums), 0)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
