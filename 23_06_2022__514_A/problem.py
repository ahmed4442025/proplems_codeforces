# 23/06/2022 20:08:01
# https://codeforces.com/contest/514/problem/A
# https://www.youtube.com/watch?v=wU51frCexTY
# https://codeforces.com/problemset/status/514/problem/A

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


def code(x):
    l = "0123443210"
    res = ""
    for c in x:
        ci = int(c)
        res += l[ci]
    if res[0] == "0":
        res = res.replace("0", "9", 1)
    print(res)


def main():
    x = input()
    code(x)


main()


# 0:15:52.874322
# 23/06/2022 20:23:53