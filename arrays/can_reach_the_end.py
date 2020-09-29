def can_reach_the_end(arr):
    '''
    Write a program which takes an array of n integers,
    where A[i] denotes the maximum you can advance from index l,
    and returns whether it is possible to advance to the last 
    index starting from the beginning of the array.
    
    [3,3,7,0,2,0,1] = true
    [3,2,0,0,2,0,7] = false
    '''
    max_i = 0
    for i in range(len(arr) - 1):
        if max_i < i:
            return False
        max_i = max(max_i, i + arr[i])
    return True
    
if __name__ == "__main__":
    test1 = [3,3,7,0,2,0,1]
    print(test1, can_reach_the_end(test1))

    test2 = [3,2,0,0,2,0,7]
    print(test2, can_reach_the_end(test2))
