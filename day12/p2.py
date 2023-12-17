lines = []
groups = []

with open('input.txt') as f:
    l = f.read().split("\n")
    for i in l:
        t = i.split()
        t[0] += ('?' + t[0]) * 4
        lines.append(t[0])
        t[1] = list(map(lambda x: int(x), t[1].split(',')))
        gLen = len(t[1])
        for j in range(4):
            for k in range(gLen):
                t[1].append(t[1][k])
        groups.append(t[1])


def memoize(f):
    memo = {}

    def helper(x, y):
        if (x, y) not in memo:
            memo[(x, y)] = f(x, y)
        return memo[(x, y)]

    return helper


@memoize
def dfs(line, group):
    if not group:
        return '#' not in line
    if len(line) - sum(group) - len(group) + 1 < 0:
        return 0
    holes = any(line[x] == '.' for x in range(group[0]))
    if len(line) == group[0]:
        return 0 if holes else 1
    use = not holes and line[group[0]] != '#'
    if line[0] == '#':
        return dfs(line[group[0] + 1:].lstrip('.'), tuple(group[1:])) if use else 0
    skip = dfs(line[1:].lstrip('.'), group)
    if not use:
        return skip
    return skip + dfs(line[group[0] + 1:].lstrip('.'), tuple(group[1:]))


def simp(line):
    for i in range(len(line) - 2, -1, -1):
        newLine = line[0]
        for i in range(1, len(line)):
            if line[i] == '.' and line[i - 1] == '.':
                continue
            newLine += line[i]
        return newLine


res = 0
for i in range(len(lines)):
    res += dfs(simp(lines[i]), tuple(groups[i]))

print(res)
