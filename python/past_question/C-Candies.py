import io
import sys

_INPUT = """\
5
3 2 2 4 1
1 2 2 2 1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = [list(map(int, input().split())) for _ in range(2)]

# 初期化
dp = [[0] * N for _ in range(2)]

dp[0][0] = A[0][0]  # 最初のアメは確定
dp[1][0] = A[0][0] + A[1][0]
for i in range(1, N):
    dp[0][i] = dp[0][i - 1] + A[0][i]  # 一行目
    dp[1][i] = max(dp[0][i], dp[1][i - 1]) + A[1][i]  # 二行目は最大値を更新していく

for i in range(2):
    print(dp[i])

print(dp[1][N - 1])
