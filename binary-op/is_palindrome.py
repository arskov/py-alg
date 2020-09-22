import sys
from reverse_digits import reverse_num

if __name__ == "__main__":
    num = int(sys.argv[1])
    print(reverse_num(num) == num)

