# 23/06/2022 16:35:19
# https://codeforces.com/contest/365/problem/A
# https://www.youtube.com/watch?v=W5SLLnni1KM
# https://codeforces.com/problemset/status/365/problem/A


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

ls = "0123456789"


def is_good(k, arr):
    for i in range(k + 1):
        if not ls[i] in arr:
            return False
    return True


def main():
    n, k = map(int, input().split())
    total = 0
    for i in range(n):
        arr = input()
        if is_good(k, arr):
            total += 1
    print(total)


main()

# 0:20:15.348454
# 23/06/2022 16:55:34
