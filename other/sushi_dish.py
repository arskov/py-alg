'''
>>> getMaximumEatenDishCount(6, [1, 2, 3, 3, 2, 1], 1)
5
>>> getMaximumEatenDishCount(6, [1, 2, 3, 3, 2, 1], 2)
4
>>> getMaximumEatenDishCount(7, [1, 2, 1, 2, 1, 2, 1], 2)
2
'''
from typing import List
from collections import deque
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    counter = 0
    eaten_dict = set()
    eaten_queue = deque()

    for i in range(N):
        dish = D[i]
        if not dish in eaten_dict:
            counter += 1
            eaten_queue.append(dish)
            eaten_dict.add(dish)
            if len(eaten_queue) > K:
                first_eaten = eaten_queue.popleft()
                eaten_dict.discard(first_eaten)

    return counter

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
