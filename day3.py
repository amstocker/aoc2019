with open("day3.txt") as f:
    data = f.read().split('\n')
    data1 = data[0].rstrip().split(',')
    data2 = data[1].rstrip().split(',')

def travel_once(pos, inst, path, steps, step):
    direction = inst[0]
    dist = int(inst[1:])
    while dist > 0:
        if direction == "R":
            pos = (pos[0] + 1, pos[1])
        if direction == "U":
            pos = (pos[0], pos[1] + 1)
        if direction == "L":
            pos = (pos[0] - 1, pos[1])
        if direction == "D":
            pos = (pos[0], pos[1] - 1)
        dist -= 1
        step += 1
        path.add(pos)
        steps[pos] = step
    return pos, step

def travel(instruction_list):
    pos = (0,0)
    step = 0
    path = set()
    steps = {}
    for inst in instruction_list:
        pos, step = travel_once(pos, inst, path, steps, step)
    return path, steps

def norm(p):
    return abs(p[0]) + abs(p[1])


# do travelling
wire1_path, wire1_steps = travel(data1)
wire2_path, wire2_steps = travel(data2)

# part 1
common = wire1_path.intersection(wire2_path)
print(min(map(norm, common)))

# part 2
print(min(map(lambda p: wire1_steps[p] + wire2_steps[p], common)))