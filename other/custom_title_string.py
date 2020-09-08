#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    res = []
    for w in s.split():
        if w[0].isalpha():
            res.append(w.title())
        else:
            res.append(w)
    return " ".join(res)

if __name__ == '__main__':
    s = "1 w 2 r 3g"
    result = solve(s)
    print(result)

