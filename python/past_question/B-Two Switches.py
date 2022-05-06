import io
import sys
_INPUT = """\
0 20 10 50
"""
sys.stdin = io.StringIO(_INPUT)

A, B, C, D = list(map(int, input().split()))

lower = min(B, D)
upper = max(A, C)

print(max(0, lower - upper))
