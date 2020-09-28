from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        s = set(deadends)
        if target in s:
            return -1
        q = deque()
        v = set()
        q.append("0000")
        v.add("0000")
        steps = -1
        while len(q) > 0:
            sz = len(q)
            steps += 1
            for i in range(sz):
                move = q.popleft()
                if move in s:
                    continue
                if move == target:
                    return steps
                for next_move in self.next_moves(move):
                    if not next_move in v:
                        v.add(next_move)
                        q.append(next_move)
        return -1
        
    def next_moves(self, move: str) -> List[str]:
        res = []
        for i in range(4):
            c = int(move[i])
            tmp = (c + 1) % 10
            res.append(move[:i] + str(tmp) + move[i + 1:])
            tmp = (c + 9) % 10
            res.append(move[:i] + str(tmp) + move[i + 1:])
        return res

if __name__ == "__main__":
    solution = Solution()
    # print(solution.next_moves("0000"))
    print(solution.openLock(["0000"], "8888"))