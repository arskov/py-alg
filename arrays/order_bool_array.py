def order_array(arr):
    left = 0
    for i in range(len(arr)):
        if not arr[i]:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1

if __name__ == "__main__":
    test1 = [True, True, False, False, True, False, False, True]
    order_array(test1)
    print(test1)