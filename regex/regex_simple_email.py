import re
import email.utils

def test_1():
    proc = re.compile(r"[a-zA-Z0-9]{1}[_\-a-zA-Z0-9]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}")
    emails = [
        'brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com'
    ]
    for i in emails:
        print(i, proc.fullmatch(i))

def test_2(tup_list):
    proc = re.compile(r"^[a-zA-Z]{1}[\_\-\.a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$")
    def valid(tup):
        return True if proc.match(tup[1]) else False

    ans = []
    for v in tup_list:
        val = email.utils.parseaddr(v)
        if valid(val):
            ans.append(val)
    for v in ans:
        print(email.utils.formataddr(v))

if __name__ == "__main__":
    test_1()
    print("---------")

    vals = [
        "this <is@valid.com>",
        "this <is_som@radom.stuff>",
        "this <is_it@valid.com>",
        "this <_is@notvalid.com>"
    ]
    test_2(vals)