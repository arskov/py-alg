"""
26. Remove Duplicates from Sorted Array

>>> s = Solution()
>>> s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
5
>>> s.removeDuplicates([1,1,2])
2
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = 0
        for r in range(len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
        return l + 1

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)