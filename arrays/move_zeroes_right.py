def move_zeroes_right(arr):
    left = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1

if __name__ == "__main__":
    test1 = [0,0,0,2,3,1,0,3,5,0,4,6,0]
    move_zeroes_right(test1)
    print(test1)