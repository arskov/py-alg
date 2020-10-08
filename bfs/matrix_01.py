"""
542. 01 Matrix

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.
Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]


>>> s = Solution()
>>> s.updateMatrix([[0,0,0],[0,1,0],[0,0,0]])
[[0, 0, 0], [0, 1, 0], [0, 0, 0]]
>>> s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
[[0, 0, 0], [0, 1, 0], [1, 2, 1]]
>>> s.updateMatrix([[0],[0],[0],[0],[0]])
[[0], [0], [0], [0], [0]]
>>> s.updateMatrix([[0],[1],[1],[1],[1]])
[[0], [1], [2], [3], [4]]
"""

from typing import List
from collections import deque
class Solution:
    
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return matrix
        rows = len(matrix)
        cols = len(matrix[0])
        
        def next_points(x, y):
            res = []
            # cur_val = matrix[x][y]
            for d in Solution.directions:
                _x = x + d[0]
                _y = y + d[1]
                if _x >= 0 and \
                   _x < rows and \
                   _y >= 0 and \
                   _y < cols and \
                   matrix[_x][_y] != 0:
                    res.append((_x, _y))
            return res
    
        v = set()
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    q.append((i, j, 0))
        while q:
            x, y, level = q.popleft()
            for np in next_points(x, y):
                if not np in v:
                    v.add((np[0], np[1]))
                    matrix[np[0]][np[1]] = level + 1
                    q.append((np[0], np[1], level + 1))
                
        return matrix

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)