from typing import List
from collections import deque

class Solution:
    '''
    752. Open the Lock
    
    You have a lock in front of you with 4 circular wheels. 
    Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. 
    The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'.
    Each move consists of turning one wheel one slot.
    The lock initially starts at '0000', a string representing the state of the 4 wheels.
    You are given a list of deadends dead ends, meaning if the lock displays any of these codes,
    the wheels of the lock will stop turning and you will be unable to open it.
    Given a target representing the value of the wheels that will unlock the lock,
    return the minimum total number of turns required to open the lock, or -1 if it is impossible.
    '''
    
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