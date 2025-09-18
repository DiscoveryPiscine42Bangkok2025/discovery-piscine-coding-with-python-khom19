import re
in_lst = re.findall(r'"(.*?)"', input())
print(in_lst[0] if len(in_lst) else "none")