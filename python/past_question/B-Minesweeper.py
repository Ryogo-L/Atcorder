import io
import sys

_INPUT = """\
6 6
#####.
#.#.##
####.#
.#..#.
#.##..
#.#...
"""
sys.stdin = io.StringIO(_INPUT)
h, w = list(map(int, input().split()))
board = []
# 右、上，左，下，右上，左上，左下，右下の差分
dw = [1, 0, -1, 0, 1, -1, -1, 1]
dh = [0, -1, 0, 1, -1, -1, 1, 1]
for i in range(h):
    board.append(list(input()))

# 各マスを全て走査
for i in range(h):
    for j in range(w):
        if board[i][j] == "#":
            continue

        num = 0
        # 空マスの場合８方向を走査する
        for k in range(8):
            nw = j + dw[k]
            nh = i + dh[k]
            # マスが存在しない場合は続ける
            if nw < 0 or w <= nw or nh < 0 or h <= nh:
                continue
            # 爆弾があればカウント
            if board[nh][nw] == "#":
                num += 1
        # 「.」を数字に置き換える
        board[i][j] = str(num)

for i in range(h):
    print("".join(board[i]))
