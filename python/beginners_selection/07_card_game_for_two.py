import io
import sys

_INPUT = """\
4
20 18 2 18
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
input_list = list(map(int, input().split()))

alice_list = []
bob_list = []

# カードの順番をソートする
input_list.sort(reverse=True)
for i in range(N):
    # カードのｎ番目と，n+1番目をそれぞれ取り出す
    # n番目がalice,n+1番目がBob
    if (i % 2 == 0):
        alice_list.append(input_list[i])
    else:
        bob_list.append(input_list[i])
result = sum(alice_list) - sum(bob_list)

# それぞれの合計値を出して，引き算する
print(result)
