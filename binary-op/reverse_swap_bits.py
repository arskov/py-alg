def swap_bits(num, i, j):
    if num & (1 << i) != num & (1 << j):
        bit_mask = (1 << i) | (1 << j)
        return num ^ bit_mask
    else:
        return num

def reverse_bits_brute_force(num, bits):
    half = bits // 2
    for i in range(half):
        num = swap_bits(num, i, bits - 1 - i)
    return num

LOOKUP_TABLE = {}
def get_lookup_table(word_size):
    global LOOKUP_TABLE
    if word_size in LOOKUP_TABLE:
        return LOOKUP_TABLE[word_size]
    table = []
    for i in range(pow(2, word_size)):
        table.append(reverse_bits_brute_force(i, word_size))
    LOOKUP_TABLE[word_size] = table
    return table

def reverse_bits_lookup_table(num, word_size):
    mask = 0
    if word_size == 8:
        mask = 0xFF
    elif word_size == 16:
        mask = 0xFFFF
    elif word_size == 32:
        mask = 0xFFFFFFFF
    else:
        raise "Word size must be 8, 16 or 32"
    lookup_table = get_lookup_table(word_size)
    result = lookup_table[num & mask] << 3 * word_size \
            | lookup_table[(num >> word_size) & mask] << 2 * word_size \
            | lookup_table[(num >> 2 * word_size) & mask] << 1 * word_size \
            | lookup_table[(num >> 3 * word_size) & mask]
    return result

if __name__ == "__main__":
    test_num = 12
    result_num = swap_bits(test_num, 0, 2)
    print("{0:0>16b} {1:0>16b}".format(test_num, result_num))
    print("-----")
    
    bits = 32
    test_num = 0b00000000_00000000_01010101_01010101
    result_num = reverse_bits_brute_force(test_num, bits)
    print("{0:0>{2}b} {1:0>{2}b}".format(test_num, result_num, bits))
    print("-----")
    
    bits = 32
    test_num = 0b00000000_00000000_01010101_01010101
    word_size = 8
    result_num = reverse_bits_lookup_table(test_num, word_size)
    print("{0:0>{2}b} {1:0>{2}b}".format(test_num, result_num, bits))
