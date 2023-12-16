import collections

grid = []

with open('input.txt') as f:
    lines = f.read().split("\n")

    for line in lines:
        grid.append([*line])

rows = len(grid)
cols = len(grid[0])
directions = [[-1,0], [0,1], [1,0], [0,-1]]
# all directions will be top clockwise
# t:0, r:1, b:2, l:3

cons = {'|':[0,2], '-':[1,3], 'L':[0,1], 'J':[0,3], '7':[2,3], 'F':[1,2], '.':[]}

def whichType(r, c):
    connections = [False, False, False, False]
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if nr in range(rows) and nc in range(cols):
            for i in cons[grid[nr][nc]]:
                cr, cc = directions[i]
                if cr == -dr and cc == -dc:
                    connections[i] = True
    if connections[0] and connections[1]:
        return '7'
    if connections[0] and connections[2]:
        return '|'
    if connections[0] and connections[3]:
        return 'F'
    if connections[1] and connections[2]:
        return 'J'
    if connections[1] and connections[3]:
        return '-'
    if connections[2] and connections[3]:
        return 'L'

loop = set()

def connects(r, c, nr, nc):
    dr, dc = nr-r, nc-c
    for i in cons[grid[nr][nc]]:
        cr, cc = directions[i]
        if cr == -dr and cc == -dc:
            return True
    return False

def bfs(row, col):
    q = collections.deque()
    loop.add((row, col))
    q.append((row, col))
    res = -1

    while q:
        tempq = q
        q = collections.deque()
        for i in range(len(tempq)):
            nr, nc = tempq[i]
            type = grid[nr][nc]
            dirs = [directions[n] for n in cons[type]]
            for dr, dc in dirs:
                r, c = nr+dr, nc+dc
                if r in range(rows) and c in range(cols) and (r,c) not in loop and connects(nr, nc, r, c):
                    q.append((r, c))
                    loop.add((r,c))
        res += 1
    return res

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            grid[r][c] = whichType(r, c)
            bfs(r, c)
            break

inside = False
previous = None
res = 0
for r in range(rows):
    for c in range(cols):
        t = grid[r][c]
        if inside and (r, c) not in loop:
            res += 1
            continue
        if (r, c) in loop:
            if grid[r][c] == "|":
                inside = not inside
                continue
            if (grid[r][c] == "7" and previous == "L") or (grid[r][c] == "J" and previous == "F"):
                inside = not inside
            if grid[r][c] in ['7', 'L', 'J', 'F']:
                previous = grid[r][c]

print(res)
