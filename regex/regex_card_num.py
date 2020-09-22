import re

dig_re = re.compile(r"^[4,5,6]{1}\d{3}[-]?\d{4}[-]?\d{4}[-]?\d{4}$")
rep_re = re.compile(r"(\d)[-]?\1[-]?\1[-]?\1")

def match(string):
    print(dig_re.match(string))
    print(rep_re.search(string))
    print(rep_re.findall(string))
if __name__ == "__main__":
    match("4123456789123456")
    print("----")
    match("5123-4567-8912-3456")
    print("----")
    match("61234-567-8912-3456")
    print("----")
    match("4123356789123456")
    print("----")
    match("5133-3367-8912-3456")
    print("----")
    match("1112222333")
