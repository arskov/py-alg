import itertools

def is_subset_using_set_logical_operators(possible_super, possible_sub):
    return ((possible_super & possible_sub) == possible_sub)

def is_subset_using_set_issubset_method(possible_super, possible_sub):
    return possible_sub.issubset(possible_super)

if __name__ == "__main__":
    A = {2, 5, 8}
    B = {2, 4, 8, 5, 6}
    print(is_subset_using_set_logical_operators(A, B))
    print(is_subset_using_set_logical_operators(B, A))
    print(is_subset_using_set_issubset_method(A, B))
    print(is_subset_using_set_issubset_method(B, A))
