"""
Range Minimum Query, several implementations
"""

from typing import List, Tuple

class RMQ_N3:
    """
    >>> test_arr = [2,4,3,1,6,7,8,9,1,7]
    >>> rmq = RMQ_N3(test_arr)
    >>> rmq.query(2, 7)
    (3, 1)
    >>> rmq.query(0, 9)
    (3, 1)
    >>> rmq.query(4, 9)
    (8, 1)
    >>> rmq.query(0, 4)
    (3, 1)
    >>> rmq.query(4, 7)
    (4, 6)
    """
    def __init__(self, arr: List[int]) -> None:
        self._len = len(arr)
        self.arr = arr
        self.rmq_arr = [None] * self._len
        for i in range(self._len):
            self.rmq_arr[i] = [0] * self._len
        for i in range(self._len):
            for j in range(self._len):
                _min = arr[i]
                _min_idx = i
                for k in range(i + 1, j + 1):
                    if arr[k] < _min:
                        _min = arr[k]
                        _min_idx = k
                self.rmq_arr[i][j] = _min_idx

    def query(self, s: int, e: int) -> Tuple[int, int]:
        if s > e or s >= self._len or e >= self._len:
            return None
        return (self.rmq_arr[s][e], self.arr[self.rmq_arr[s][e]])

class RMQ_N2:
    """
    >>> test_arr = [2,4,3,1,6,7,8,9,1,7]
    >>> rmq = RMQ_N2(test_arr)
    >>> rmq.query(2, 7)
    (3, 1)
    >>> rmq.query(0, 9)
    (3, 1)
    >>> rmq.query(4, 9)
    (8, 1)
    >>> rmq.query(0, 4)
    (3, 1)
    >>> rmq.query(4, 7)
    (4, 6)
    """
    def __init__(self, arr: List[int]) -> None:
        self._len = len(arr)
        self.arr = arr
        self.rmq_arr = [None] * self._len
        for i in range(self._len):
            self.rmq_arr[i] = [0] * self._len
            self.rmq_arr[i][i] = i
        for i in range(self._len):
            for j in range(i + 1, self._len):
                if self.arr[self.rmq_arr[i][j-1]] <= self.arr[j]:
                    self.rmq_arr[i][j] = self.rmq_arr[i][j-1]
                else:
                    self.rmq_arr[i][j] = j

    def query(self, s: int, e: int) -> Tuple[int, int]:
        if s > e or s >= self._len or e >= self._len:
            return None
        return (self.rmq_arr[s][e], self.arr[self.rmq_arr[s][e]])

class RMQ_N_SQRTN:
    """
    >>> test_arr = [2,4,3,1,6,7,8,9,1,7]
    >>> rmq = RMQ_N_SQRTN(test_arr)
    >>> rmq.query(2, 7)
    (3, 1)
    >>> rmq.query(0, 9)
    (3, 1)
    >>> rmq.query(4, 9)
    (8, 1)
    >>> rmq.query(0, 4)
    (3, 1)
    >>> rmq.query(4, 7)
    (4, 6)
    """
    def __init__(self, arr: List[int]) -> None:
        import math
        self._len = len(arr)
        sq = math.sqrt(self._len)
        self.rmq_segments = math.ceil(sq)
        self.rmq_seg_size = math.floor(sq)
        self.arr = arr
        self.rmq_arr = [-1] * self.rmq_segments
        for i in range(self._len):
            j = i // self.rmq_seg_size
            if self.rmq_arr[j] == -1:
                self.rmq_arr[j] = i
                continue
            if arr[i] <= arr[self.rmq_arr[j]]:
                self.rmq_arr[j] = i

    def query(self, start: int, end: int) -> Tuple[int, int]:
        if start > end or start >= self._len or end >= self._len:
            return None
        min_idx = -1
        min_val = float('inf')
        start_segment_idx = start // self.rmq_seg_size
        start_segment_end = (start_segment_idx + 1) * self.rmq_seg_size - 1
        end_segment_idx = end // self.rmq_seg_size
        end_segment_start = end_segment_idx * self.rmq_seg_size
        for i in range(start, start_segment_end + 1):
            if self.arr[i] < min_val:
                min_idx = i
                min_val = self.arr[i]
        for i in range(start_segment_idx + 1, end_segment_idx):
            if self.arr[self.rmq_arr[i]] < min_val:
                min_idx = self.rmq_arr[i]
                min_val = self.arr[self.rmq_arr[i]]
        for i in range(end_segment_start, end + 1):
            if self.arr[i] < min_val:
                min_idx = i
                min_val = self.arr[i]
        return (min_idx, min_val)
        
class RMQ_SEGMENT_TREE:
    """
    >>> test_arr = [2,4,3,1,6,7,8,9,1,7]
    >>> rmq = RMQ_SEGMENT_TREE(test_arr)
    >>> rmq.query(2, 7)
    (3, 1)
    >>> rmq.query(0, 9)
    (8, 1)
    >>> rmq.query(4, 9)
    (8, 1)
    >>> rmq.query(0, 4)
    (3, 1)
    >>> rmq.query(4, 7)
    (4, 6)
    """
    def __init__(self, arr: List[int]) -> None:
        n = len(arr)
        self.arr = arr
        self.segment_tree = [-1] * (4 * n)
        self._build_segment_tree(1, 0, n - 1)

    def _build_segment_tree(self, node: int, l: int, r: int):
        if l == r:
            self.segment_tree[node] = l # store the index, not a value
        else:
            mid = l + (r - l) // 2
            self._build_segment_tree(2*node, l, mid)
            self._build_segment_tree(2*node + 1, mid+1, r)
            idx1 = self.segment_tree[2*node]
            idx2 = self.segment_tree[2*node + 1]
            # check values at indexes in the original array
            # and store the index of the minimum value
            if self.arr[idx1] < self.arr[idx2]:
                self.segment_tree[node] = idx1
            else:
                self.segment_tree[node] = idx2

    def _query_helper(self, node: int, b: int, e: int, l: int, r: int):
        if l > e or r < b:
            return -1 # not a valid index
        if l <= b and r >= e:
            return self.segment_tree[node]
        mid = b + (e - b) // 2
        q1 = self._query_helper(2*node, b, mid, l, r)
        q2 = self._query_helper(2*node + 1, mid + 1, e, l, r)
        # we manipulate indexes in the segment_tree
        if q1 == -1:
            return q2
        if q2 == -1:
            return q1
        # then we check values
        if self.arr[q1] < self.arr[q2]:
            return q1
        else:
            return q2

    def query(self, start: int, end: int) -> Tuple[int, int]:
        idx = self._query_helper(1, 0, len(self.arr) - 1, start, end)
        return (idx, self.arr[idx])


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    # test_arr = [2,4,3,1,6,7,8,9,1,7]
    # rmq_1 = RMQ_N_SQRTN(test_arr)
    # print(rmq_1.query(4, 7)) # expect (4, 6)
    # test_arr = [2,4,3,1,6,7,8,9,1,7]
    # rmq_1 = RMQ_N2(test_arr)
    # print(rmq_1.query(4, 7)) # expect (4, 6)