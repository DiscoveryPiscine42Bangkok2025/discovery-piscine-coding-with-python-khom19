import re
in_lst = re.findall(r'"(.*?)"', input())
if len(in_lst) != 1:
    print("none")
else:
    words = input("What was the parameter? ")
    if words != in_lst[0]:
        print("Nope, sorry...")
    else:
        print("Good job!")