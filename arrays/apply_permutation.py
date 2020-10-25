"""
Apply permutation to array.

>>> arr = [-1,1,2,0]
>>> perm = [3,2,1,0]
>>> apply_permutation1(perm.copy(), arr.copy())
[0, 2, 1, -1]
>>> apply_permutation2(perm.copy(), arr.copy())
[0, 2, 1, -1]
"""

def apply_permutation1(perm, arr):
    res =  [None] * len(arr)
    for i, p in enumerate(perm):
        res[p] = arr[i]
    return res

def apply_permutation2(perm, arr):
    for i in range(len(arr)):
        nex = i
        while perm[nex] >= 0:
            arr[i], arr[perm[nex]] = arr[perm[nex]], arr[i]
            tmp = perm[nex]
            perm[nex] -= len(arr)
            nex = tmp
    return arr

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
