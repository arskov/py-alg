# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
import sys
import time
from collections import deque
from datetime import timedelta

def solution():
    with open(sys.path[0] + '/calculations_on_tree_input_1.txt') as in_file:

        n, q = [int(x) for x in in_file.readline().split()]
        adj_lst = [None] * (n + 1)
        for _ in range(n - 1):
            a, b = [int(x) for x in in_file.readline().split()]
            if adj_lst[a] is None:
                adj_lst[a] = []
            if adj_lst[b] is None:
                adj_lst[b] = []
            adj_lst[a].append(b)
            adj_lst[b].append(a)

        # build LCA and RMQ support stuctures
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
        # print(*euler)
        # print(*height)
        # print(*first)

        segment_tree = [-1] * (len(euler) * 4)
        # print("seg tree len", len(segment_tree))

        def build_tree(node: int, l: int, r: int):
            if l == r:
                segment_tree[node] = euler[l]
                return
            mid = l + (r - l) // 2
            build_tree(2 * node, l, mid)
            build_tree(2 * node + 1, mid + 1, r)
            val1 = segment_tree[2 * node]
            val2 = segment_tree[2 * node + 1]
            segment_tree[node] = val1 if height[val1] < height[val2] else val2

        build_tree(1, 0, len(euler) - 1)
        # print(*segment_tree)

        def lca(node: int, b: int, e: int, l: int, r: int) -> int:
            if b > r or e < l:
                return -1
            if b >= l and e <= r:
                return segment_tree[node]
            mid = b + (e - b) // 2
            ql = lca(2 * node, b, mid, l, r)
            qr = lca(2 * node + 1, mid + 1, e, l, r)
            if ql == -1:
                return qr
            if qr == -1:
                return ql
            return ql if height[ql] < height[qr] else qr

        # distance on segment tree
        dist_cache = dict()
        def dist(s: int, e: int) -> int:
            l = first[s]
            r = first[e]
            if l > r:
                l, r = r, l
            p = (l, r)
            if p in dist_cache:
                return dist_cache[p]
            lca_node = lca(1, 0, len(euler) - 1, l, r)
            # print("lca for {} and {} is {}".format(s, e, lca_node))
            d = (height[s] - height[lca_node]) + (height[e] - height[lca_node])
            dist_cache[p] = d
            return d

        def generate_pairs(l):
            if len(l) <= 2:
                return [l]
            return [*itertools.combinations(l, 2)]

        # sets = []
        for _ in range(q):
            k = int(in_file.readline())
            s = [int(x) for x in in_file.readline().split()]
            # sets.append(s)
            pairs = generate_pairs(s)
            result = 0
            for pair in pairs:
                if len(pair) <= 1:
                    break
                result += pair[0] * pair[1] * dist(pair[0], pair[1])
            print(result % 1000000007)
        
        # for s in sets:
        #     pairs = generate_pairs(s)
        #     result = 0
        #     for pair in pairs:
        #         if len(pair) <= 1:
        #             break
        #         result += pair[0] * pair[1] * dist(pair[0], pair[1])
        #     print(result % 1000000007)

if __name__ == "__main__":
    start = time.time()
    solution()
    end = time.time()
    print("Execution time:", end - start)