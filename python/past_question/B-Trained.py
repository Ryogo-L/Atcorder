import io
import sys
_INPUT = """\
5
3
3
4
2
4
"""
sys.stdin = io.StringIO(_INPUT)
N = int(input())

button_list = [int(input()) for _ in range(N)]
is_exit = False
count = 0
a_i = button_list[0]

for _ in range(N):
    count += 1
    if a_i == 2:
        print(count)
        is_exit = True
        break
    a_i = button_list[a_i - 1]


if not is_exit:
    print(-1)
