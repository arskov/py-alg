# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import time
import math
import random
from collections import deque
from datetime import timedelta

""" THIS IS NOT COMPLETED """
def solution():
    sys.setrecursionlimit(3000)
    with open(sys.path[0] + '/calculations_on_tree_input_20.txt') as in_file:

        n, q = [int(x) for x in in_file.readline().split()]
        # build an adjacency list
        adj_lst = [None] * (n + 1)
        for _ in range(n - 1):
            a, b = [int(x) for x in in_file.readline().split()]
            if adj_lst[a] is None:
                adj_lst[a] = []
            if adj_lst[b] is None:
                adj_lst[b] = []
            adj_lst[a].append(b)
            adj_lst[b].append(a)
        print("adjacency list is ready")

        query_set = [set() for _ in range(q)]
        query_set_result = [0] * q

        for i in range(q):
            in_file.readline()
            query_set[i] = [int(x) for x in in_file.readline().split()]


        _size = n + 1 # node's values start from 1
        depth = [0] * _size
        ancestor = [0] * _size
        dsu = [0] * _size
        visited = set()

        def dsu_get(v):
            if dsu[v] == v:
                return v
            else:
                dsu[v] = dsu_get(dsu[v])
                return dsu[v]

        def dsu_unite(a, b, new_ancestor):
            a = dsu_get(a)
            b = dsu_get(b)
            if random.randint(0, 32000) % 2:
                a, b = b, a
            dsu[a] = b
            ancestor[b] = new_ancestor

        def dfs(v, d):
            visited.add(v)
            dsu[v] = v
            ancestor[v] = v
            depth[v] = d
            for child in adj_lst[v]:
                if not child in visited:
                    dfs(child, d + 1)
                    dsu_unite(v, child, v)
            for child in adj_lst[v]:
                if child in visited:
                    for i in range(q):
                        if (v in query_set[i]) and (child in query_set[i]):
                            lca = ancestor[dsu_get(child)]
                            query_set_result[i] += v * child * (depth[v] - depth[lca] + depth[child] - depth[lca])

        dfs(1, 1)
        print("dfs completed")

        for r in query_set_result:
            print(r % 1000000007)
        

if __name__ == "__main__":
    start = time.time()
    solution()
    end = time.time()
    print("Execution time:", end - start)