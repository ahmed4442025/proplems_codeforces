# 23/06/2022 14:57:10
# https://codeforces.com/problemset/problem/318/A
# https://www.youtube.com/watch?v=w7gZx99Efzs

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


def code(n, k):
    if n % 2 == 0:
        mid = n / 2
    else:
        mid = (n + 1) / 2

    if k <= mid:
        print(k * 2 - 1)
    else:
        print(int((k - mid) * 2))


def main():
    # n, k = map(int, input().split())
    inp = input().split(' ')
    n = int(inp[0])
    k = int(inp[1])
    code(n, k)


main()

# 23/06/2022 15:30:28
# 0:37:56.813218
# 23/06/2022 15:35:06