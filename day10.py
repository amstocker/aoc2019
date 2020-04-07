with open("day10.txt") as f:
    data = f.read().strip().split('\n')
    grid = [list(l) for l in data]

W = len(grid[0])
H = len(grid)

# get positions of asteroids
asteroids = set([])
for y in range(H):
    for x in range(W):
        if grid[y][x] == '#':
            asteroids.add((x, y))

# determine possible slopes
slopes = set([(0, 1), (0, -1), (1, 0), (-1, 0)])
for dx in range(-W + 1, W):
    for dy in range(-W + 1, H):
        if (dx == 0) or (dy == 0):
            continue
        for (dx0, dy0) in slopes:
            if (dx * dy0 == dx0 * dy) and (dx * dx0 > 0):
                if (abs(dx) < abs(dx0)) or (abs(dy) < abs(dy0)):
                    slopes.remove((dx0, dy0))
                    slopes.add((dx, dy))
                break
        else:
            slopes.add((dx, dy))

# compute line-of-sight counts
line_of_sight_data = {t: 0 for t in asteroids}
for (x0, y0) in asteroids:
    for (dx, dy) in slopes:
        x = x0 + dx
        y = y0 + dy
        while (0 <= x < W) and (0 <= y < H):
            if (x, y) in asteroids:
                line_of_sight_data[(x, y)] += 1
                break
            x += dx
            y += dy

# part 1
print(max(line_of_sight_data.values()))