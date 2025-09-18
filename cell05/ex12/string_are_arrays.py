import re
in_str = str(re.findall(r'"(.*?)"', input()))
num = in_str.count("z")
if num and in_str:
    print("z"*num)
else:
    print("none")