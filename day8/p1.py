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

cur = 'AAA'

i = 0
res = 0

while cur != 'ZZZ':
    if directions[i] == 'L':
        cur = adj[cur][0]
    else:
        cur = adj[cur][1]
    i = (i + 1) % dirLen
    res += 1

print(res)

