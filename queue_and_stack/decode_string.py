"""
394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string 
inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid;
No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not 
contain any digits and that digits are only for those repeat numbers, k. 
For example, there won't be input like 3a or 2[4].

>>> solution = Solution()
>>> solution.decodeString("3[a]2[bc]")
'aaabcbc'
>>> solution.decodeString("3[a2[c]]")
'accaccacc'
>>> solution.decodeString("2[abc]3[cd]ef")
'abcabccdcdcdef'
>>> solution.decodeString("abc3[cd]xyz")
'abccdcdcdxyz'

"""
class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return s
        mul_buf = []
        mul_stack = []
        str_buf = []
        str_stack = []
        for c in s:
            if c.isdigit():
                mul_buf.append(c)
            elif c == "[":
                str_stack.append(str_buf)
                str_buf = []
                mul_stack.append(int("".join(mul_buf)))
                mul_buf = []
            elif c == "]":
                tmp = str_buf * mul_stack.pop()
                if str_stack:
                    str_buf = []
                    str_buf.extend(str_stack.pop())
                    str_buf.extend(tmp)
                else:
                    str_buf = tmp
            else:
                str_buf.append(c)
        return "".join(str_buf)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)