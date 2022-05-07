import io
import sys
_INPUT = """\
10 8
"""
sys.stdin = io.StringIO(_INPUT)

N, K = list(map(int, input().split()))

num = N ** N
answer = K * ((K - 1) ** (N - 1))

print(answer)
