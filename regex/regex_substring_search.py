import re

def find_first_occurance_of_repeated_letter(input_str):
    """Finds the first alfanumeric letter which is repeated in the string. Regex backreference."""
    # input_str = "__commit__"
    m = re.search(r"([0-9a-zA-Z]{1}).*?\1", input_str, re.I | re.M)
    return m.group(1)

def find_vowels_between_consonants(input_str):
    """Finds more then 2 vowels between consonants. Regex positive lookahead"""
    # input_str = "abaabaabaabaae"
    m = re.finditer(r"[qwrtypsdfghjklzxcvbnm]([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])", input_str, re.I)
    return [i.group(1) for i in m] if m else None

def find_substring_indexes(whole_str, token_str):
    # input_str = "baaadaa"
    reg = re.compile(r"{}".format(token_str))
    n = len(whole_str)
    i = 0
    result = []
    while i < n:
        m = reg.search(whole_str, i)
        if not m:
            break
        result.append((m.start(), m.end()))
        i = m.start() + 1
    return result

if __name__ == "__main__":
    print(find_first_occurance_of_repeated_letter("__commit__"))
    print(find_first_occurance_of_repeated_letter("1101234567"))
    print(find_first_occurance_of_repeated_letter("12345671"))
    print(find_first_occurance_of_repeated_letter("12345672"))
    print("-----")
    print(find_vowels_between_consonants("abaabaabaabaae"))
    print("-----")
    print(find_substring_indexes("abaabaabaabaae", "aa"))
    print(find_substring_indexes("aaadaa", "aa"))
