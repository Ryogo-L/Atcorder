import io
import sys

_INPUT = """\
77 42 36
"""
sys.stdin = io.StringIO(_INPUT)
a, b, c = list(map(int, input().split()))

for i in range(1, b):
    if (i) * a % b == c:
        print('YES')
        exit()
print('NO')
