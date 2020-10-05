"""44. Recursion"""

import sys
sys.setrecursionlimit(104)


i = 0


def mac():
    global i
    i += 1
    print("akhil", i)
    mac()


mac()
