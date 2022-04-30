import io
import sys

_INPUT = """\
20 2 5
"""
sys.stdin = io.StringIO(_INPUT)
input_list = list(map(int, input().split()))

N = input_list[0]
A = input_list[1]
B = input_list[2]
result = 0

for i in range(N):
    # N以下の整数を読み込む
    target = i + 1
    each_digit = [int(i) for i in str(target)]
    # 各桁を取り出して整数化して足す
    sum_num = sum(each_digit)
    # 合計値を比較し，条件を満たせば総和を算出
    if (sum_num >= A and sum_num <= B):
        result += target

print(result)
