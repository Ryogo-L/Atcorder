import io
import sys

_INPUT = """\
110
"""
sys.stdin = io.StringIO(_INPUT)

l_1 = list(input())

for i in range(len(l_1)):
    l_1[i] = int(l_1[i])

print(l_1.count(1))
