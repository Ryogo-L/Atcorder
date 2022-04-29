import io
import sys

_INPUT = """\
3 3
"""
sys.stdin = io.StringIO(_INPUT)

l_1 = list(map(int, input().split()))
a = l_1[0]
b = l_1[1]

r = a * b

if r % 2 == 0:
    print("Even")
else:
    print("Odd")


""""出力例
Even
Odd
"""