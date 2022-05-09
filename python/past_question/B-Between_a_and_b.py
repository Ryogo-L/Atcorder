import io
import sys
_INPUT = """\
1 1000000000000000000 3
"""
sys.stdin = io.StringIO(_INPUT)

a, b, x = list(map(int, input().split()))


def division(n):
    return n // x


if a == 0:
    print(division(b) + 1)
else:
    print(int(division(b) - division(a - 1)))
