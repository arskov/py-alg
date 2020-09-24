from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if nums is None or len(nums) == 0:
            return []
        _count = Counter(nums)
        ans = [(v,k) for k, v in _count.items()]
        _len = len(ans)
        
        def partition(start, end):
            pivot_idx = end
            pivot_val = ans[pivot_idx][0]
            j = start
            for i in range(start, end):
                if ans[i][0] < pivot_val:
                    ans[j], ans[i] = ans[i], ans[j]
                    j += 1
            ans[j], ans[pivot_idx] = ans[pivot_idx], ans[j]
            return j
        
        def quickselect(start, end):
            if start == end:
                return start
            mid = partition(start, end)
            if mid == _len - k:
                return mid
            elif mid < _len - k:
                return quickselect(mid + 1, end)
            else:
                return quickselect(start, mid - 1)
        
        m = quickselect(0, _len - 1)
        
        return [v[1] for v in ans[m:]]

if __name__ == "__main__":
    solution = Solution()
    test = [1,2,3,1,2,3,4,5,2,3,4,3]
    print(sorted(test, reverse = True))
    print(solution.topKFrequent(test, 3))