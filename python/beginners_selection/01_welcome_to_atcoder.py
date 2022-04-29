import io
import sys

_INPUT = """\
1
2 3
test
"""
sys.stdin = io.StringIO(_INPUT)

l_1 = int(input())
l_2 = list(map(int, input().split()))
l_3 = input()

i = l_2[0]
k = l_2[1]
sum = l_1 + i + k

print("{} {}".format(sum, l_3))


'''
6 test
'''
