lines = []
groups = []

with open('input.txt') as f:
    l = f.read().split("\n")
    for i in l:
        t = i.split()
        lines.append(t[0])
        groups.append(list(map(lambda x: int(x), t[1].split(','))))


def isValid(line, group):
    i = 0
    t = []
    for c in line:
        if c == '.' and i != 0:
            t.append(i)
            i = 0
        elif c == '#':
            i += 1
    if i != 0:
        t.append(i)
    return t == group

def dfs(line, group):
    if line.count('?') == 0:
        if isValid(line, group):
            return 1
        else:
            return 0

    i = line.find('?')
    return dfs(line[:i] + '.' + line[i+1:], group) + dfs(line[:i] + '#' + line[i+1:], group)

res = 0

for i in range(len(lines)):
    res += dfs(lines[i], groups[i])

print(res)

# This is solution is terrible btw and i know it is