"""
150	Evaluate Reverse Polish Notation    

Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:
    Division between two integers should truncate toward zero.
    The given RPN expression is always valid. That means the expression would always 
    evaluate to a result and there won't be any divide by zero operation.

>>> solution = Solution()
>>> solution.evalRPN(["2", "1", "+", "3", "*"])
9
>>> solution.evalRPN(["4", "13", "5", "/", "+"])
6
>>> solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
22
"""

from typing import List

class Solution:

    ops = "+-*/"

    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        stack = []
        for tok in tokens:
            if tok in Solution.ops:
                b = stack.pop()
                a = stack.pop()
                c = None # eval("a {} b".format(tok))
                if tok == "+":
                    c = a + b
                elif tok == "-":
                    c = a - b
                elif tok == "*":
                    c = a * b
                elif tok == "/":
                    c = a / b
                stack.append(int(c))
            else:
                stack.append(int(tok))
        return stack[-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)