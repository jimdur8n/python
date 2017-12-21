import math


print("hello world\n")

m = [9, 14, 24]

def modify(k):
    k.append(39)
    print("k =", k)

modify(m)


def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

print(math.sqrt(100))
