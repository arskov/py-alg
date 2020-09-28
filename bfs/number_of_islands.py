from collections import deque
from typing import List

class Solution:
    
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        vis = set()
        rows = len(grid)
        cols = len(grid[0])
        counter = 0
        for i in range(rows):
            for j in range(cols):
                if (not (i, j) in vis) and grid[i][j] == "1":
                    counter += 1
                    self.bfs(i, j, grid, vis)
        return counter
    
    def is_valid(self, grid, node):
        return node[0] >= 0 and \
                node[0] < len(grid) and \
                node[1] >= 0 and \
                node[1] < len(grid[0]) and \
                grid[node[0]][node[1]] == "1"
    
    def bfs(self, i, j, grid, vis):
        q = deque()
        node = (i, j)
        q.append(node)
        vis.add(node)
        while len(q) > 0:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                for d in Solution.directions:
                    next_node = (node[0] + d[0], node[1] + d[1])
                    if self.is_valid(grid, next_node) and not next_node in vis:
                        vis.add(next_node)
                        q.append(next_node)
        return
                    
if __name__ == "__main__":
    s = Solution()
    test = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(s.numIslands(test))