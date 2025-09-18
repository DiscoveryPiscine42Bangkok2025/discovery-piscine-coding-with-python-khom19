import re
in_lst = re.findall(r'"(.*?)"', input())
if len(in_lst) > 0:
    for word in in_lst:
        if word[-3:] != "ism":
            print(word+"ism")
else:
    print("none")