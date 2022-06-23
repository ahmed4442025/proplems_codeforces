# 23/06/2022 23:03:50
# https://codeforces.com/problemset/problem/9/A
# https://www.youtube.com/watch?v=5T1yiz9-jZo
# https://codeforces.com/problemset/status/9/problem/A

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
    l = ["1/1", "5/6", "2/3", "1/2", "1/3", "1/6", "0/1"]
    print(l[max(n, k) - 1])


def main():
    n, k = map(int, input().split())
    code(n, k)


main()

# 0:09:08.811324
# 23/06/2022 23:12:58