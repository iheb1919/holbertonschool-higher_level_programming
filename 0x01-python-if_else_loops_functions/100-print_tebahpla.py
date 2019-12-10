#!/usr/bin/python3
for i in range(122, 96, - 1):
    j = i
    if i % 2 != 0:
       j = i - 32
    else:
        print("{}".format(chr(j)), end="")
