import io
import sys

_INPUT = """\
11 11
...#####...
.##.....##.
#..##.##..#
#..##.##..#
#.........#
#...###...#
.#########.
.#.#.#.#.#.
##.#.#.#.##
..##.#.##..
.##..#..##.
"""
sys.stdin = io.StringIO(_INPUT)
h, w = list(map(int, input().split()))
canvas = []

# 右、上，左，下の差分
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(h):
    canvas.append(list(input()))

is_exit_hashtag = False

hashtag_count = 0
for i in range(h):
    for j in range(w):
        if canvas[i][j] != ".":
            hashtag_count += 1
            # 上下左右に＃があるかチェック
            for k in range(4):
                # 現在地+差分
                nx = j + dx[k]
                ny = i + dy[k]

                if nx >= w or nx < 0 or ny >= h or ny < 0:
                    continue
                if canvas[ny][nx] == "#" or canvas[ny][nx] == "BLACK":
                    canvas[i][j] = 'BLACK'

dot_count = 0
black_count = 0
for i in range(h):
    for j in range(w):
        if canvas[i][j] == '.':
            dot_count += 1
        if canvas[i][j] == 'BLACK':
            black_count += 1

if dot_count == h * w or hashtag_count == black_count:
    print('Yes')
else:
    print('No')
