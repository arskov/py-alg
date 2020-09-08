from collections import OrderedDict
l = "abcdefghijklmnopqrstuvwxyz"[::-1]
print(l)
d = OrderedDict.fromkeys(l)
print(d)
sorted(d)
