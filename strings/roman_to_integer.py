"""
13. Roman to Integer

>>> s = Solution()
>>> s.romanToInt('III')
3
>>> s.romanToInt('IV')
4
>>> s.romanToInt('IX')
9
>>> s.romanToInt('LVIII')
58
>>> s.romanToInt('MCMXCIV')
1994

"""

class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        _len = len(s)
        
        number = 0
        prev = 0
        for c in s[::-1]:
            if prev and prev > d[c]:
                number -= d[c]
            else:
                number += d[c]
            prev = d[c]
            
        return number

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)