grid = []
rows, cols = -1, -1

with open('input.txt') as f:
    lines = f.read().split("\n")
    rows = len(lines)
    cols = len(lines[0])

    for line in lines:
        if line == '.' * cols:
            grid.append([*line])
            rows += 1
        grid.append([*line])

addedCols = []

for c in range(cols):
    col = ""
    for r in range(rows):
        col += grid[r][c]
    if col == '.' * rows:
        addedCols.append(c)

addedCols.sort(reverse=True)

for col in addedCols:
    for r in range(rows):
        grid[r].insert(col, '.')
    cols += 1

def manhattanDistance(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

coords = {}
i = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '#':
            coords[i] = (r, c)
            i += 1

galaxies = len(coords)

res = 0

for n in range(galaxies):
    for m in range(n+1, galaxies):
        d = manhattanDistance(coords[n], coords[m])
        res += d

print(res)

