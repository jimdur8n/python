import math
import os

print("hello world\n")

m = [9, 14, 24]
m += ['dog']

def modify(k):
    k.insert(1, 39)
    print("k =", k)

modify(m)
del m[1]

def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

print(math.sqrt(100))
