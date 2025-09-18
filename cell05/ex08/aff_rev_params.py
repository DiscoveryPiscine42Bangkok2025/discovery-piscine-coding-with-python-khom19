import re
in_lst = re.findall(r'"(.*?)"', input())
print("none") if len(in_lst) < 2 else [print(in_lst[i]) for i in range(len(in_lst)-1,-1,-1)]