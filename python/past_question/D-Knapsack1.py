import io
import sys

_INPUT = """\
5 5
1 1000000000
1 1000000000
1 1000000000
1 1000000000
1 1000000000
"""
sys.stdin = io.StringIO(_INPUT)

N, W = list(map(int, input().split()))
# print(N, W)

items = [list(map(int, input().split())) for _ in range(N)]
w = [items[i][0] for i in range(N)]
v = [items[i][1] for i in range(N)]
# print(w, v)

dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(W + 1):
        if j >= w[i]:
            dp[i + 1][j] = max(dp[i][j - w[i]] + v[i], dp[i][j])
        else:
            dp[i + 1][j] = dp[i][j]


for i in range(N + 1):
    print(dp[i])

print(dp[N][W])


