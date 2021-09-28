#!/usr/bin/env python3
import bisect
from typing import List, Tuple

def get_art_count(N: int, C: str, X: int, Y: int) -> int:
    '''
    >>> count_range([1,3,5,7,9], 1, 3)
    2
    >>> count_range([1,3,5,7,9], 0, 3)
    2
    >>> count_range([1,3,5,7,9], 0, 15)
    5
    >>> count_range([1,3,5,7,9], 3, 3)
    1
    >>> count_range([1,3,5,7,9], 0, 2)
    1
    >>> count_range([1,3,5,7,9], 0, 0)
    0
    >>> count_range([1,3,5,7,9], 2, 2)
    0
    >>> count_range([1,3,5,7,9], 0, 0)
    0
    >>> count_range([1,3,5,7,9], 10, 10)
    0

    >>> get_art_count(3,'BAB', 1, 1)
    0
    >>> get_art_count(3,'PAB', 1, 1)
    1
    >>> get_art_count(3,'BAP', 1, 1)
    1
    >>> get_art_count(3,'PAB', 1, 10)
    1
    >>> get_art_count(3,'BAP', 1, 10)
    1
    >>> get_art_count(12,'PP...AA...BB', 1, 10)
    8
    >>> get_art_count(9,'B...A...P', 1, 10)
    1
    >>> get_art_count(6,'PABPAB', 1, 2)
    2
    >>> get_art_count(5, 'APABA', 1, 2)
    1
    >>> get_art_count(5, 'APABA', 2, 3)
    0
    >>> get_art_count(8, '.PBAAP.B', 1, 3)
    3
    >>> get_art_count(13, '.P.A.B.B.A.PP', 1, 3)
    3
    '''
    dic = dict()
    dic['P'] = []
    dic['A'] = []
    dic['B'] = []
    count = 0

    for i in range(N):
        if C[i] == 'P':
            dic['P'].append(i)
        elif C[i] == 'A':
            dic['A'].append(i)
        elif C[i] == 'B':
            dic['B'].append(i)
    
    dic['P'].sort()
    dic['A'].sort()
    dic['B'].sort()

    count = 0
    # P(i) A(j) B(k) - right
    # B(i) A(j) P(k) - left
    for j in dic['A']:
        if j + X > N - 1 or j - X < 0:
            continue
        right_min_idx = j + X
        right_max_idx = j + Y if j + Y < N else N
        left_min_idx = 0 if j - Y < 0 else j - Y
        left_max_idx = j - X
 
        b_right_count = count_range(dic['B'], right_min_idx, right_max_idx)
        p_right_count = count_range(dic['P'], left_min_idx, left_max_idx)
        right_count = b_right_count * p_right_count

        b_left_count = count_range(dic['B'], left_min_idx, left_max_idx)
        p_left_count = count_range(dic['P'], right_min_idx, right_max_idx)
        left_count = b_left_count * p_left_count

        count += right_count + left_count

    return count

def count_range(l: List[int], i_start: int, i_end: int) -> int:
    range_start_idx = bisect.bisect_left(l, i_start)
    if range_start_idx == len(l):
        return 0

    range_end_idx = bisect.bisect_right(l, i_end)
    if range_end_idx == len(l):
        return range_end_idx - range_start_idx
    elif l[range_end_idx] != i_end:
        range_end_idx -= 1
    
    if range_end_idx < range_start_idx:
        return 0
    else:
        return range_end_idx - range_start_idx + 1

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
