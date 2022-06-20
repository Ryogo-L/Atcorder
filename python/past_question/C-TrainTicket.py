import io
import sys

_INPUT = """\
1222
"""
sys.stdin = io.StringIO(_INPUT)

S = input()
for i in range(2 ** 3):  # 全探索
    f = S[0]

    for j in range(3):
        if ((i >> j) & 1):  # 各桁をチェック
            f += '+'
        else:
            f += '-'
        f += str(S[j+1])
    if eval(f) == 7:
        f += '=7'
        print(f)
        exit()