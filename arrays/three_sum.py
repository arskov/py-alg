"""
15. 3Sum

>>> s = Solution()
>>> s.threeSum([-1,0,1,2,-1,-4])
{(-1, 0, 1), (-1, -1, 2)}
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        
        def two_sum(start, need):
            memo = set()
            pairs = []
            i = start
            while i < len(nums):
                complement = need - nums[i]
                if complement in memo:
                    pairs.append((nums[i], complement))
                    next_i = i + 1
                    while next_i < len(nums) and nums[i] == nums[next_i]:
                        next_i += 1
                else:
                    next_i = i + 1
                memo.add(nums[i])
                i = next_i
            return pairs
        
        res = set()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            pairs = two_sum(i + 1, 0 - nums[i])
            if pairs:
                for p in pairs:
                    val = [nums[i], p[0], p[1]]
                    val.sort()
                    res.add((val[0], val[1], val[2]))
        return res

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)