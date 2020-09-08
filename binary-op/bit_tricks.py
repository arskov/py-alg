def cyclic_xor():
    """Function show a cyclic XOR of 1"""
    res = 0
    for i in range(10):
        res ^= 1
        print("{0:0>16b}".format(res))

def diff_x_and_x_minus_one_1():
    """Remember this useful thing. You can combine x with x - 1 in order to achive interesting cases.
    This trick CLEARS the last set bit"""

    x = 122
    print("{0:0>16b}".format(x))
    print("{0:0>16b}".format(x - 1))
    # This trick CLEARS the last set bit
    x = x & (x - 1)
    print("{0:0>16b}".format(x))

def diff_x_and_x_minus_one_2():
    """Remember this useful thing. You can combine x with x - 1 in order to achive interesting cases.
    This trick REMAINS ONLY the last set bit"""
    
    x = 122
    print("{0:0>16b}".format(x))
    print("{0:0>16b}".format(x - 1))
    print("{0:0>16b}".format(~(x - 1)))
    # This trick REMAINS ONLY the last set bit
    x = x & ~(x - 1)
    print("{0:0>16b}".format(x))

def print_some_powers_of_two():
    for i in range(0,128,2):
        print("{0:0>128b}".format(2**i))


def is_power_of_two():
    """Trick for checking the power of two. 
    The power of two has only one set bit. 
    See previous function which prints powers of two."""

    for i in range(128 + 1):
        is_power_of_rwo = ((i & (~(i - 1))) ^ i == 0)
        print("{0:d} - {0:0>32b} - {1}".format(i, is_power_of_rwo))

def main():
    diff_x_and_x_minus_one_1()
    print("-----")
    diff_x_and_x_minus_one_2()

if __name__ == "__main__":
    main()
