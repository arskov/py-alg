import sys

def reverse_num(x):
    result = 0
    tmp = x if x > 0 else -x
    while tmp:
        rem = tmp % 10
        result = result * 10 + rem
        tmp //= 10
    return result if x > 0 else -result

if __name__ == "__main__":
    print(reverse_num(int(sys.argv[1])))
