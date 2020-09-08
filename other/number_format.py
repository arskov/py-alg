def print_formatted(number):
    """Outputs numbers from 1 to number in Decimal, Octal, Hex, Bin formats
    and aligns to the width of a binary representation"""

    w = len("{0:b}".format(number))
    for i in range(1, number + 1):
        print("{1:>{0}d} {1:>{0}o} {1:>{0}x} {1:>{0}b}".format(w, i))

if __name__ == '__main__':
    n = 17
    print_formatted(n)