def move_zeroes_left(arr):
    '''
    Note! Relative order of non-zero values should not change
    '''
    left = len(arr) - 1
    for i in range(left, -1, -1):
        if arr[i] != 0:
            arr[i], arr[left] = arr[left], arr[i]
            left -= 1

if __name__ == "__main__":
    test1 = [0,0,0,2,3,1,0,3,5,0,4,6,0]
    print(test1)
    move_zeroes_left(test1)
    print(test1)