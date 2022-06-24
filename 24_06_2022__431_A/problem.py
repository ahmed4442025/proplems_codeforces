# 24/06/2022 23:13:45
# https://codeforces.com/contest/431/problem/A
# https://www.youtube.com/watch?v=mJYiMoX4t0k
# https://codeforces.com/problemset/status/431/problem/A

import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def test():
    o = open(os.path.join(__location__, 'data.txt'), encoding="UTF-8")
    data = o.readlines()
    for line in data:
        line = line.replace("\n", '')
        print(line)


# ==================================================


def code(dic, s):
    dic_c = {"1": 0, "2": 0, "3": 0, "4": 0}
    for c in s:
        dic_c[c] += 1
    res = 0
    for k in dic_c:
        res += dic[k] * dic_c[k]
    print(res)


def main():
    l = list(map(int, input().split()))
    dic = {
        "1": l[0], "2": l[1], "3": l[2], "4": l[3],
    }
    s = input()
    code(dic, s)


main()

# 0:12:21.922391
# 24/06/2022 23:26:06