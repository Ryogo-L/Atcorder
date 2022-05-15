# ナップサック問題練習
N = 5
length = 10
li = [4, 7, 8, 5, 1]

money = 500
price = [150, 200, 250, 200, 50]

# 簡略化
money = money // 50
price = list(map(lambda x: x // 50, price))

print(price, money)

# 表を0で初期化
dp = [[0 for _ in range(length + 1)] for _ in range(N + 1)]

# dp[0]はこのfor文では関係ない 次の行を変更していく作業
for i in range(N):
    for j in range(money + 1):
        if j >= price[i]:
            # その価格の最大の組み合わせ
            dp[i + 1][j] = max(dp[i][j - price[i]] + li[i], dp[i][j])
        else:
            dp[i + 1][j] = dp[i][j]
for i in dp:
    print(i)
