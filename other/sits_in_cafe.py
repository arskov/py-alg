from typing import List
import math


def count(num: int, k: int) -> int:
    return math.ceil(num / (k + 1))


def max_additional_din_count(N: int, K: int, M: int, S: List[int]) -> int:
    '''
    >>> max_additional_din_count(10, 1, 2, [2,6])
    3
    >>> max_additional_din_count(15, 2, 3, [11, 6, 14])
    1
    >>> max_additional_din_count(3, 1, 1, [1])
    1
    >>> max_additional_din_count(3, 1, 1, [2])
    0
    >>> max_additional_din_count(3, 1, 1, [3])
    1
    '''
    if N <= 0 or N == K:
        return 0
    if not S or M == 0:
        return count(N, K)
    res = 0
    S.sort()
    prev = None
    for i in S:
        a = 1 if prev is None else prev + K + 1
        b = i - K - 1
        if b >= a:
            res += count(b - a + 1, K)
        prev = i
    if prev + K < N:
        res += count(N - (prev + K + 1) + 1, K)

    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
