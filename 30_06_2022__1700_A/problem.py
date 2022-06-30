# 30/06/2022 15:02:49
# https://codeforces.com/problemset/problem/1700/A
# 
# https://codeforces.com/problemset/status/1700/problem/A

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


def code(rows, columns):
    res = subc(rows, columns) + subr(columns)
    res -= columns
    print(int(res))


def subr(columnsn):
    res = (1 + columnsn) / 2
    res *= columnsn
    return res


def subc(rown, columnsn):
    minn = columnsn
    maxn = columnsn * rown
    res = (maxn + minn) / 2
    res *= rown
    return res


def main():
    n = int(input())
    for i in range(n):
        rows, columns = map(int, input().split())
        code(rows, columns)


main()
