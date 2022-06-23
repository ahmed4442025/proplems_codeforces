# https://codeforces.com/contest/535/problem/B
# https://www.youtube.com/watch?v=NPVp5BntYZ4&list=PLPt2dINI2MIa5tPrd1wO1pY8w5XuxRbhR&index=25
import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# n = input()

def get_current(cell_n):
    total = 0
    for i in range(cell_n - 1):
        i += 1
        total += 2 ** (i)
    return total


def calc_index(n="4"):
    total = get_current(len(n)) + 1
    current = 2 ** len(n)
    for c in n:
        current /= 2
        if c == "7":
            total += current

    print(int(total))


def test():
    o = open(os.path.join(__location__, 'data.txt'), encoding="UTF-8")
    data = o.readlines()
    for line in data:
        line = line.replace("\n", '')
        # print(line)
        calc_index(line)


def main():
    calc_index(input())

main()