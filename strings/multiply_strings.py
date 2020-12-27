"""
43. Multiply Strings

>>> s = Solution()
>>> s.multiply("123","33")
'4059'
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return ""
        if num1 == "0" or num2 == "0":
            return "0"
        result = "0"
        res_mul = 1
        for i in range(len(num1) - 1, -1, -1):
            a = int(num1[i])
            tmp_row = 0
            mul_row = 1
            mul_carry = 0
            for j in range(len(num2) - 1, -1, -1):
                b = int(num2[j])
                tmp = a * b + mul_carry
                mul_carry = tmp // 10
                rem = tmp % 10
                tmp_row += rem * mul_row
                mul_row *= 10
            tmp_row += mul_carry * mul_row
            tmp_row *= res_mul
            res_mul *= 10
            result = self.add(result, tmp_row)
        return result
    
    def add(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)