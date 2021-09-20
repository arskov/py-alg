'''
>>> invert_string("ABA")
'BAB'
>>> invert_string("AABB")
'BBAA'
>>> invert_string("BBB")
'AAA'
>>> invert_string("ABABAB")
'BABABA'
'''


def invert_string(s: str) -> str:
    return ''.join(['A' if c == 'B' else 'B' for c in s])


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
