# 25/06/2022 23:42:05
# https://codeforces.com/problemset/problem/143/A
# https://www.youtube.com/watch?v=cmMkGSMHTKE
# https://codeforces.com/problemset/status/143/problem/A

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


def code():
    r1, r2 = map(int, input().split())
    c1, c2 = map(int, input().split())
    d1, d2 = map(int, input().split())

    x2 = (d2 - c1 + r1) / 2
    x1 = r1 - x2
    x3 = c1 - x1
    x4 = d1 - x1

    if checkV(x1) == -1 or checkV(x2) == -1 or checkV(x3) == -1 or checkV(x4) == -1:
        return

    if x1 == x2 or x1 == x3 or x1 == x4 or x2 == x3 or x2 == x4 or x3 == x4:
        print("-1")
        return

    if r1 == x1 + x2 and c1 == x1 + x3 and d1 == x1 + x4 and r2 == x3 + x4 and c2 == x2 + x4 and d2 == x2 + x3:
        print(f'{int(x1)} {int(x2)}')
        print(f'{int(x3)} {int(x4)}')
        return
    print('-1')

def checkV(x):
    if x > 9 or x < 1:
        print('-1')
        return -1
    return 0

def main():
    code()


main()
