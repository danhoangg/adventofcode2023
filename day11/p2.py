grid = []
rows, cols = -1, -1

emptyRows = []
emptyCols = []

with open('input.txt') as f:
    lines = f.read().split("\n")
    rows = len(lines)
    cols = len(lines[0])

    for i, line in enumerate(lines):
        if line == '.' * cols:
            emptyRows.append(i)
        grid.append([*line])

for c in range(cols):
    col = ""
    for r in range(rows):
        col += grid[r][c]
    if col == '.' * rows:
        emptyCols.append(c)

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
        er, ec = 0, 0
        for r in emptyRows:
            if min(coords[n][0], coords[m][0]) < r < max(coords[n][0], coords[m][0]):
                er += 1
        for c in emptyCols:
            if min(coords[n][1], coords[m][1]) < c < max(coords[n][1], coords[m][1]):
                ec += 1

        x1, y1 = coords[n]
        x2, y2 = coords[m]
        if x1 >= x2:
            x1 += (1000000-1) * er
        else:
            x2 += (1000000-1) * er

        if y1 >= y2:
            y1 += (1000000-1) * ec
        else:
            y2 += (1000000-1) * ec

        res += manhattanDistance((x1, y1), (x2, y2))

print(res)

