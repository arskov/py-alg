# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
import sys
import time
import math
from collections import deque
from datetime import timedelta

def solution():
    sys.setrecursionlimit(3000)
    with open(sys.path[0] + '/calculations_on_tree_input_1.txt') as in_file:

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

        # build support stuctures for RMQ and LCA
        visited = set()
        euler = []
        height = [None] * (n + 1)
        first = [None] * (n + 1)

        def dfs(node: int, h: int):
            visited.add(node)
            height[node] = h
            first[node] = len(euler)
            euler.append(node)
            for child in adj_lst[node]:
                if not child in visited:
                    dfs(child, h + 1)
                    euler.append(node)
        
        dfs(1, 1)
        print("euler path is ready")

        euler_len = len(euler)
        # precompute logarithm values
        logt = [0] * (euler_len + 1)
        for i in range(2, euler_len + 1):
            logt[i] = logt[i // 2] + 1

        # build a sparce table
        K = logt[euler_len]
        st = [None] * (K + 1)
        for i in range(0, K + 1):
            st[i] = [None] * euler_len
        for j in range(0, euler_len):
            st[0][j] = euler[j]
        for i in range(1, K + 1):
            j = 0
            while (j + (1 << i)) <= euler_len:
                st[i][j] = min(st[i-1][j], st[i-1][j + (1<<(i-1))])
                j += 1
        print("sparse table is ready")

        def lca(l: int, r: int) -> int:
            p = logt[r - l + 1]
            return min(st[p][l], st[p][r-(1<<p)+1])

        # use a cache for distance values
        dist_cache = dict()
        def dist(s: int, e: int) -> int:
            l = first[s]
            r = first[e]
            if l > r:
                l, r = r, l
            p = (l, r)
            if p in dist_cache:
                return dist_cache[p]
            lca_node = lca(l, r)
            # print("lca for {} and {} is {}".format(s, e, lca_node))
            d = (height[s] - height[lca_node]) + (height[e] - height[lca_node])
            dist_cache[p] = d
            return d

        for _ in range(q):
            k = int(in_file.readline())
            print("array length is", k)
            s = [int(x) for x in in_file.readline().split()]
            # sort 
            s.sort()
            k = 0
            # remove duplicates
            for i in range(len(s)):
                if s[k] != s[i]:
                    s[k] = s[i]
                    k += 1
            print("processed array length is", k + 1)
            # do for all pairs
            result = 0
            for i in range(k + 1):
                for j in range(i + 1, k + 1):
                    result += s[i] * s[j] * dist(s[i], s[j])
            print(result % 1000000007)
        

if __name__ == "__main__":
    start = time.time()
    solution()
    end = time.time()
    print("Execution time:", end - start)