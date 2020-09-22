regex_integer_in_range = r"^[1-9][\d]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=[\d]\1)"	# Do not delete 'r'.

import re

def match(string):
    print(re.match(regex_integer_in_range, string))
    print(re.findall(regex_alternating_repetitive_digit_pair, string))
    return (bool(re.match(regex_integer_in_range, string)) and
        len(re.findall(regex_alternating_repetitive_digit_pair, string)) < 2)

if __name__ == "__main__":
    print(match("100000"))
    print(match("999999"))
    print(match("110000"))
    print(match("523563"))
