import io
import sys

_INPUT = """\
3
8 5 40
"""
sys.stdin = io.StringIO(_INPUT)

q = int(input())
l_1 = list(map(int, input().split()))


def isEven(value):
    if not value % 2 == 0:
        return False
    value /= 2
    return True


def isSuccess(list):
    print('計算スタート')
    try:
        for i in list:
            if isEven(i):
                return True
            else:
                raise Exception()
        print(l_1)
    except Exception:
        return False


count = 0

try:
    if not isSuccess(l_1):
        raise Exception()
    count += 1
    print(count)

except Exception:
    print(count)


#　操作始める
    # for i in range(q):
    # if isEven(l_1[i]):
    #     l_1[i] /= 2
    #     print("ok")
    # else:
    #     print(0)
    #     break

    # if isExit:
    #     # 操作続ける
    # else：
    #     # 操作終わり