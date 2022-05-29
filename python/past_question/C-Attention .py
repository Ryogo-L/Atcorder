import io
import sys

_INPUT = """\
12
WEWEWEEEWWWE
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = list(input())

# W==>Eの配列
e_list = []
w_list = []
e_count, w_count = [0, 0]
for i in range(N):
    w_list.append(w_count)
    if S[i] == 'W':
        w_count += 1


S.reverse()
# E==>Wの配列
for i in range(N):
    e_list.append(e_count)
    if S[i] == 'E':
        e_count += 1
e_list.reverse()

# print(w_list)
# print(e_list)

ans = 10 ** 100
for i in range(N):
    ans = min(ans, (w_list[i] + e_list[i]))

print(ans)


# 別解
# N = int(input())
# S = list(input())

# # Eの個数で初期化(累積和)
# count = S.count('E')
# ans = count
# # 左端1番目からリーダーをずらしながら全探索
# for i in range(len(S)):
#     # 初期値から、Eである場合マイナス1、Wである場合プラス１していく
#     if S[i] == 'E':
#         count -= 1
#         ans = min(count, ans)
#     else:
#         count += 1

# print(ans)
# N = int(input())
# S = list(input())

# # Eの個数で初期化(累積和)
# count = S.count('E')
# ans = count
# # 左端1番目からリーダーをずらしながら全探索
# for i in range(len(S)):
#     # 初期値から、Eである場合マイナス1、Wである場合プラス１していく
#     if S[i] == 'E':
#         count -= 1
#         ans = min(count, ans)
#     else:
#         count += 1

# print(ans)

# 参考
# http://takaxyz.com/2018/07/11/atcoder-bc098-c-attention/
# https://scrapbox.io/yu2ta7ka/AtCoder_ARC_098_C_-_Attention_(300_%E7%82%B9)