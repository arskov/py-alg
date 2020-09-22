def quicksort(array):
    quicksort_helper(array, 0, len(array) - 1)
    return array

def quicksort_helper(array, s, e):
    if s >= e:
        return
    pi = pivot(array, s, e)
    quicksort_helper(array, s, pi - 1)
    quicksort_helper(array, pi + 1, e)

def pivot(array, s, e):
    pivot_value = array[e]
    i = s
    for j in range(s, e):
        if array[j] < pivot_value:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[e] = array[e], array[i]
    return i

if __name__ == "__main__":
    array = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print(quicksort(array))

