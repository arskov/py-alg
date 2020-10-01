"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

>>> solution = Solution()
>>> solution.isValid("()")
True
>>> solution.isValid("[]")
True
>>> solution.isValid("{}")
True
>>> solution.isValid("([{}])")
True
>>> solution.isValid("({[(())]})")
True
>>> solution.isValid("({[(())")
False
>>> solution.isValid("({)}")
False
"""
class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return False
        stack = []
        for c in s:
            if "(" == c or "[" == c or c == "{":
                stack.append(c)
                continue
            elif ")" == c:
                if stack and stack[-1] == "(":
                    stack.pop()
                    continue
                else:
                    return False
            elif "]" == c:
                if stack and stack[-1] == "[":
                    stack.pop()
                    continue
                else:
                    return False
            elif "}" == c:
                if stack and stack[-1] == "{":
                    stack.pop()
                    continue
                else:
                    return False
        if stack:
            return False
        else:
            return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()