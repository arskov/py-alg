import sys

def power_recursive(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    elif y == 2:
        return x * x
    else:
        if y % 2 == 0:
            return power_recursive(x, y // 2) * power_recursive(x, y // 2)
        else:
            return power_recursive(x, (y - 1) // 2) * power_recursive(x, (y - 1) // 2) * x

def power_iterative(x, y):
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result

if __name__ == "__main__":
    print(power_recursive(int(sys.argv[1]), int(sys.argv[2])))
    print(power_iterative(int(sys.argv[1]), int(sys.argv[2])))
