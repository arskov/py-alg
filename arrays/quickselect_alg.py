import random

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """Quickselect"""
        if nums is None:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return min(nums[0], min(nums[1], nums[2]))
        _len = len(nums)
        k_smallest_idx = _len - 3
        return self.select({*nums}, 0, _len - 1, k_smallest_idx)
    
    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot_idx = random.randint(left, right)
        pivot_val = nums[pivot_idx]
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        k = left
        for i in range(left, right):
            if nums[i] < pivot_val:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
        nums[k], nums[right] = nums[right], nums[k]
        return k
        
    def select(self, nums: List[int], left: int, right: int, k: int) -> int:
        if left == right:
            return nums[left]
        pi = self.partition(nums, left, right)
        if pi == k:
            return nums[pi]
        elif pi < k:
            return self.select(nums, pi + 1, right, k)
        else:
            return self.select(nums, left, pi - 1, k)
        