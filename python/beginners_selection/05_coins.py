import io
import sys

_INPUT = """\
5
1
0
150
"""
sys.stdin = io.StringIO(_INPUT)

a = int(input())
b = int(input())
c = int(input())
sum = int(input())

result = 0
count = 0
# 全通り足していく
for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            result = (i * 500) + (j * 100) + (k * 50)
            # sumと一致した場合のみカウントする
            if result == sum:
                count += 1

print(count)
