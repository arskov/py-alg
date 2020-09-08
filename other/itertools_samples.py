import os
import sys
from itertools import product
from itertools import groupby

def find_max_sum_of_squares_across_all_combinations():
    """Shows usage of the product function from itertools"""

    with open(sys.path[0] + "/itertools_input_1.txt") as f:
        k, m = [int(i) for i in f.readline().split()]
        list_all = []

        for j in range(k):
            list_all.append([int(i) for i in f.readline().split()][1:])
        max_res = float('-inf')

        for comb in product(*list_all):
            val = sum([i**2 for i in comb]) % m
            max_res = val if val > max_res else max_res

        print(max_res)

def groupby_sample():
    """Shows usage of the groupby function from itertools"""
    
    s = "111223344321"
    print(*[(len(list(v)), int(k)) for k, v in groupby(s)])

if __name__ == "__main__":
    find_max_sum_of_squares_across_all_combinations()
    print("-----")
    groupby_sample()