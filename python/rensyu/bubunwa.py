# 部分和の練習

N = 5
length = 10
li = [4, 7, 8, 5, 1]

# 表をFalseで初期化
dp = [[False for _ in range(length + 1)] for _ in range(N + 1)]

for i in range(N):
    for j in range(length):
        if dp[i][j]:
            dp[i + 1][j] = True  # 次の行にTrueスライド
            if j + li[i] <= length:
                dp[i + 1][j + li[i]] = True

for i in dp:
    print(i)
