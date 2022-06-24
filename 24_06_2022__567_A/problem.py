# 24/06/2022 23:35:53
# https://codeforces.com/contest/567/problem/A
# https://www.youtube.com/watch?v=gc4BEAw0pbs
# https://codeforces.com/problemset/status/567/problem/A

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


def code(l):
    if len(l) == 2:
        res = l[1] - l[0]
        if res < 0:
            res = 0 - res
        print_values(res, res)
        print_values(res, res)
        return
    max_v = l[-1] - l[0]
    min_v = l[0] - l[1]
    print_values(max_v, min_v)
    for i in range(1, len(l) - 1):
        max_v = max(l[-1] - l[i], l[i] - l[0])
        min_v = min(l[i + 1] - l[i], l[i] - l[i - 1])
        print_values(max_v, min_v)
    max_v = l[-1] - l[0]
    min_v = l[-1] - l[-2]
    print_values(max_v, min_v)


def print_values(max_v, min_v):
    if max_v < 0:
        max_v = 0 - max_v
    if min_v < 0:
        min_v = 0 - min_v
    print(f"{min_v} {max_v}")


def main():
    input()
    l = list(map(int, input().split()))
    code(l)


main()

# 0:21:53.100386
# 24/06/2022 23:57:46