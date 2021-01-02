"""
Hackerrank: Array Pairs
https://www.hackerrank.com/challenges/array-pairs/problem
"""
import sys
from bisect import bisect_right
from bisect import bisect_left

def solve_1(arr):
    pair_count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] * arr[j] <= _max(arr, i, j):
                pair_count += 1
    return pair_count

def _max(arr, s, e):
    max_val = 0
    for i in range(s, e + 1):
        max_val = max(max_val, arr[i])
    return max_val

def solve_2(arr):
    if len(arr) <= 1:
        return 0
    arr.sort()
    pair_count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] * arr[j] <= arr[len(arr)-1]:
                pair_count += 1
    return pair_count

if __name__ == '__main__':
    with open(sys.path[0] + '/array_pairs_1_input_1.txt') as in_file:
        in_file.readline()
        arr = [int(x) for x in in_file.readline().strip().split()]
        print(solve_1(arr))
        # print(solve_2(arr))