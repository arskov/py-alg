"""
HackerRank: QHEAP1
https://www.hackerrank.com/challenges/qheap1/problem
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import heapq

hp = []
deleted = set()

n = int(input())
for i in range(n):
    command = [int(x) for x in input().split()]
    if command[0] == 1:
        heapq.heappush(hp, command[1])
    elif command[0] == 2:
        if hp[0] == command[1]:
            heapq.heappop(hp)
        else:
            deleted.add(command[1])
    elif command[0] == 3:
        while hp[0] in deleted:
            rem = heapq.heappop(hp)
            deleted.remove(rem)
        print(hp[0])