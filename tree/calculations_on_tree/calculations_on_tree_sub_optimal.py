# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
import sys
import time
from collections import deque
from datetime import timedelta

def solution():
    with open(sys.path[0] + '/calculations_on_tree_input_1.txt') as in_file:

        n, q = [int(x) for x in in_file.readline().split()]
        _a = time.time()
        adj_lst = [None] * (n + 1)
        adj_mat = [None] * (n + 1)
        for i in range(n + 1):
            adj_mat[i] = [None] * (n + 1)
            adj_mat[i][i] = 0
        for _ in range(n - 1):
            a, b = [int(x) for x in in_file.readline().split()]
            adj_mat[a][b] = 1
            adj_mat[b][a] = 1
            if adj_lst[a] is None:
                adj_lst[a] = []
            if adj_lst[b] is None:
                adj_lst[b] = []
            adj_lst[a].append(b)
            adj_lst[b].append(a)

        def dist(src, dst):
            if src == dst:
                return 0
            q = deque()
            v = set()
            q.append((src, 0))
            v.add(src)
            while q:
                cur = q.popleft()
                if cur[0] == dst:
                    return cur[1]
                adj = adj_lst[cur[0]]
                if adj:
                    for j in adj:
                        if not j in v:
                            v.add(j)
                            q.append((j, cur[1] + 1))
            return 0
        
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if adj_mat[i][j] == None:
                    adj_mat[i][j] = adj_mat[j][i] = dist(i, j)
        _b = time.time()
        #print("Graph ready time: {:.6f} sec".format(_b - _a))
        sets = []
        for _ in range(q):
            k = int(in_file.readline())
            s = [int(x) for x in in_file.readline().split()]
            sets.append(s)
            
        def generate_pairs(l):
            if len(l) <= 2:
                return [l]
            return [*itertools.combinations(l, 2)]

        for s in sets:
            pairs = generate_pairs(s)
            result = 0
            for pair in pairs:
                if len(pair) <= 1:
                    break
                result += pair[0] * pair[1] * adj_mat[pair[0]][pair[1]]
            print(result % 1000000007)
        _c = time.time()
        #print("Calculations time: {:.6f} sec".format(_c - _b))

if __name__ == "__main__":
    start = time.time()
    solution()
    end = time.time()
    print("Execution time:", end - start)