import io
import sys

_INPUT = """\
4
10
8
8
6
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
input_list = [int(input()) for i in range(n)]

# 重複を削除して，要素数を調べる
mochis = list(set(input_list))
mochis.sort(reverse=True)
print(len(mochis))
