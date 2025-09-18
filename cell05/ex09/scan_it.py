import re
in_lst = re.findall(r'"(.*?)"', input())
try:
    search = in_lst.pop(0)
    in_lst = in_lst.pop()
    print(in_lst.count(search))
except:
    print("none")