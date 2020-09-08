def two_sum(arr, n):
    d = dict()
    for i, v in enumerate(arr):
        complement = n - v
        if complement in d:
            return (d[complement], i)
        d[v] = i
    return -1

if __name__ == "__main__":
    test = [2,4,6,8,1,3,5,3]
    print(two_sum(test, 11))