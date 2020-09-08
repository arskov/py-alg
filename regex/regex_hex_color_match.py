import re
import os
import sys
proc = re.compile(r":?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})", re.I)

def color_match(file_path):
    global proc
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            m = proc.findall(line)
            for i in m:
                print(i)

if __name__ == "__main__":
    color_match(sys.path[0] + "/hex_color_match_1.txt")
    print("------------")
    color_match(sys.path[0] + "/hex_color_match_2.txt")