import io
import os
from datetime import datetime

# problemLink = "https://codeforces.com/problemset/problem/318/A"
# problemYT = "https://www.youtube.com/watch?v=w7gZx99Efzs"

problemLink = input("https://codeforces.com/problemset/problem/318/A :\n")
problemYT = input("https://www.youtube.com/watch?v=w7gZx99Efzs :\n")


def get_333A(link):
    p_info = problemLink.split("/")
    a = p_info[-1]
    n = p_info[-2]
    if n == "problem":
        n = p_info[-3]
    return [n, a]


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
template_path = os.path.join(__location__, "template.txt")


def get_dir_name():
    my_date = datetime.now().strftime("%d_%m_%Y")
    p_info = get_333A(problemLink)
    d_Name = f"{my_date}__{p_info[0]}_{p_info[1]}"
    return d_Name


def get_template_code():
    my_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    template = open(template_path).read()
    p_info = get_333A(problemLink)
    sol_link = f"# https://codeforces.com/problemset/status/{p_info[0]}/problem/{p_info[1]}\n"
    head = f"# {my_date}\n"
    head += f"# {problemLink}\n"
    head += f"# {problemYT}\n"
    head += sol_link
    return head + template


def create_code_file(new_path):
    o = open((new_path + "\\problem.py"), 'w')
    template = get_template_code()
    o.write(template)
    o.close()


def create_files(dir_name):
    dir_path = os.path.join(__location__, dir_name)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
        open((dir_path + "\\data.txt"), 'a').close()
        open(dir_path + "\\notes.txt", 'a').close()
        create_code_file(dir_path)


def main():
    create_files(get_dir_name())


main()

# 1:17:14.665990
# 26/06/2022 00:59:19