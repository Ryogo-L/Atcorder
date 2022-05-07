import io
import sys
_INPUT = """\
100000
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())

num = 1
for i in range(N):
    num = num * (i + 1) % (10 ** 9 + 7)

print(num)
