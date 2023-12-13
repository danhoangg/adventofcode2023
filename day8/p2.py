import math

lines = []

with open('input.txt') as f:
    lines = f.read().split("\n")

directions = lines[0]
dirLen = len(directions)

adj = {}

for i in range(2, len(lines)):
    t = lines[i].split()
    val = t[0]
    left = t[2][1:-1]
    right = t[3][:-1]

    adj[val] = [left, right]

cur = []
for node in adj:
    if node[-1] == 'A':
        cur.append(node)

i = 0
res = []
for j in range(len(cur)):
    count = 0
    while True:
        done = True
        if directions[i] == 'L':
           cur[j] = adj[cur[j]][0]
        else:
           cur[j] = adj[cur[j]][1]
        if cur[j][-1] != 'Z':
            done = False
        i = (i + 1) % dirLen
        count += 1

        if done:
            break
    res.append(count)

print(math.lcm(*res))

