"""
HackerRank: Jesse and Cookies
https://www.hackerrank.com/challenges/jesse-and-cookies/problem
"""

#!/bin/python3

import os
import sys
import heapq
#
# Complete the cookies function below.
#
def cookies(k, A):
    heapq.heapify(A)
    count = 0
    while A[0] < k and len(A) > 1:
        new_cookie = heapq.heappop(A) + 2 * heapq.heappop(A)
        heapq.heappush(A, new_cookie)
        count += 1
    return count if A[0] >= k else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    A = list(map(int, input().rstrip().split()))
    result = cookies(k, A)
    fptr.write(str(result) + '\n')
    fptr.close()