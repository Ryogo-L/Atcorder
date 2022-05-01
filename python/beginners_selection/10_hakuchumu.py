import io
import sys

_INPUT = """\
erasedream
"""
sys.stdin = io.StringIO(_INPUT)

s = input()


def solve(query):
    while True:
        for flag in ("dream", "dreamer", "erase", "eraser"):
            # 語尾からflagが存在するか見ていく(er問題が解決する)
            if query.endswith(flag):
                # 語尾からflagの文字数分取り除く
                query = query[:-len(flag)]
                break
        # 語尾に存在しなければNOで抜ける
        else:
            print("NO")
            break
        # queryがなくなったらYESで抜ける
        if not query:
            print("YES")
            break


solve(s)
