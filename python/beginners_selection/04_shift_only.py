import io
import sys

_INPUT = """\
3
8 40 40
"""
sys.stdin = io.StringIO(_INPUT)

q = int(input())
l_1 = list(map(int, input().split()))

count = 0
print(q)
print(l_1)

# 繰り返せるだけ繰り返す
while True:
    exist_odd = False

    # 奇数があるかどうか判定
    for i in range(q):
        if l_1[i] % 2 != 0:
            exist_odd = True

    # 奇数があれば抜ける
    if exist_odd:
        break

    # 条件に合う場合は処理を行う
    for i in range(q):
        l_1[i] = l_1[i] // 2

    count += 1

print(count)
