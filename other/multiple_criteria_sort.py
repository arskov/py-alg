
def custom_criteria_sort(input_str):
    """Builds a tuple list with the first field indicating a sort priority"""
    tuple_list = []
    for c in input_str:
        item = [0, 0]
        if c.isupper():
            item[0] = 1
        if c.islower():
            item[0] = 0
        if c.isdigit():
            if int(c) % 2 == 1:
                item[0] = 2
            else:
                item[0] = 3
        item[1] = c
        tuple_list.append(tuple(item))
    # now the sorted function sorts tuples acoordingly to field order
    return "".join([x[1] for x in sorted(tuple_list)])

if __name__ == "__main__":
    print(custom_criteria_sort("Sorting1234"))