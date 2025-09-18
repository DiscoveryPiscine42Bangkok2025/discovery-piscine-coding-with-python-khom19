import re
print(f"Number of parameters: {len(re.findall(r'"(.*?)"', input()))}.")