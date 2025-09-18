import re
in_lst = re.findall(r'"(.*?)"', input())
if len(in_lst) > 0:
    print(f"parameters: {len(in_lst)}")
    for word in in_lst:
        print(f"{word}: {len(word)}")
else:
    print("none")