import os

a = []
b = []

with open('day1/day1_input.txt', 'r') as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            num1, num2 = map(int, parts)
            a.append(num1)
            b.append(num2)
        else:
            print(f"Skipping malformed line: {line.strip()}")

a.sort()
b.sort()
distance = 0
for i in range(len(a)):
    distance += abs(int(a[i]) - int(b[i]))

print(distance)
#ans is 2113135
