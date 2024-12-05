import re

content: str
with open("day3/day3_input.txt", "r") as file:
    content = file.read()
pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern, content)
ans = 0
# int_matches = [(int(a)), (int(b)) for a, b in matches]
for i in matches:
    mul = int(i[0]) * int(i[1])
    ans += mul
print(ans)
