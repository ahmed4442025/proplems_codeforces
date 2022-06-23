# 23/06/2022 23:23:29
# https://codeforces.com/problemset/problem/490/A
# https://www.youtube.com/watch?v=2jJA1PCOrgg
# https://codeforces.com/problemset/status/490/problem/A

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


def code(n, students):
    l1 = []
    l2 = []
    l3 = []
    for i in range(len(students)):
        c = students[i]
        if c == "1":
            l1.append(i + 1)
        elif c == "2":
            l2.append(i + 1)
        else:
            l3.append(i + 1)
    min_len = min(len(l1), len(l2), len(l3))
    print(min_len)
    for i in range(min_len):
        print(f"{l1[i]} {l2[i]} {l3[i]}")


def main():
    n = int(input())
    students = input().split()
    code(n, students)


main()

# 0:17:18.310164
# 23/06/2022 23:40:47