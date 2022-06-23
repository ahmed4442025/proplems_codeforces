# 23/06/2022 23:46:45
# https://codeforces.com/contest/225/problem/A
# https://www.youtube.com/watch?v=AU4cdWZrKNA
# https://codeforces.com/problemset/status/225/problem/A

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


def code(n, top):
    b = 7 - top
    for i in range(n):
        l = list(map(int, input().split()))
        l.append(7 - l[0])
        l.append(7 - l[1])
        if top in l:
            print("NO")
            return

    print('YES')


def main():
    n = int(input())
    top = int(input())
    code(n, top)


main()

# 0:26:07.532991
# 24/06/2022 00:12:52
