"""
8. String to Integer (atoi)

>>> s = Solution()
>>> s.myAtoi("42")
42
>>> s.myAtoi("-42")
-42
>>> s.myAtoi("    42")
42
>>> s.myAtoi("    -42")
-42
>>> s.myAtoi("word and 42")
0
>>> s.myAtoi("  42 and word")
42

"""
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        int_min = -2147483648
        int_max = 2147483647
        is_number = False
        is_negative = False
        overflow = False
        numbers = []
        number = 0
        for c in s:
            if c.isdigit():
                if not is_number:
                    is_number = True
                if c == '0' and len(numbers) == 0:
                    continue
                numbers.append(int(c))
            else:
                if is_number:
                    break
                else:
                    if c == '-':
                        is_number = True
                        is_negative = True
                        continue
                    elif c == '+':
                        is_number = True
                        continue
                    elif c == ' ':
                        continue
                    else:
                        break
            if len(numbers) > 10:
                overflow = True
                break
        if overflow:
            return int_min if is_negative else int_max
        mul = 1
        while numbers:
            number += mul * int(numbers.pop())
            mul *= 10
        number = -number if is_negative else number
        if number <= int_min:
            return int_min
        if number >= int_max:
            return int_max
        return number
        
if __name__ == "__main__":
    # solution = Solution()
    # print(solution.myAtoi("     -42    "))
    import doctest
    doctest.testmod(verbose=True)