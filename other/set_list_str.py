from collections import OrderedDict
if __name__ == "__main__":
    alf = "aabbccddeeffgghhiiggkkllmmnnooppqqrrssttuuvvwwxxyyzz"
    k = 3
    parts = [alf[i:i+k] for i in range(0, len(alf), k)]
    for part in parts:
        print("".join(OrderedDict.fromkeys(part)))