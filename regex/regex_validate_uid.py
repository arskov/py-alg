import re

proc = re.compile(r"^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})[a-zA-Z0-9]{10}$")

if __name__ == "__main__":
    print("Valid") if proc.match("B1CD102354") else print("Invalid")
    print("Valid") if proc.match("B1CDEF2354") else print("Invalid")