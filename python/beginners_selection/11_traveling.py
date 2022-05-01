import io
import sys

_INPUT = """\
2
3 1 2
6 1 1
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
input_lists = [list(map(int, input().split())) for i in range(n)]

t1, x1, y1 = 0, 0, 0
res = None
for input_list in input_lists:
    t2, x2, y2 = input_list
    dt, dx, dy = t2 - t1, x2 - x1, y2 - y1
    able = abs(dx) + abs(dy)
    # print([dt, dx, dy])
    # ｘとｙの絶対値の和（マンハッタン距離）が移動時間を超える場合はNO
    if dt < able:
        res = "No"
        print(res)
        break
    # 移動可能距離と移動時間の偶奇判定（その場にとどまることは出来ないため）
    elif dt % 2 != (able) % 2:
        res = "No"
        print(res)
        break
    else:
        pass
    t1, x1, y1 = input_list

if res is None:
    print("Yes")
else:
    pass
