with open("day3.txt") as f:
    data = f.read().split('\n')
    wire1 = data[0].rstrip().split(',')
    wire2 = data[1].rstrip().split(',')

def travel_once(pos, inst, path):
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
        path.add(pos)
        dist -= 1
    return pos

def travel(inst_list):
    pos = (0,0)
    path = set()
    for inst in inst_list:
        pos = travel_once(pos, inst, path)
    return path

def norm(p):
    return abs(p[0]) + abs(p[1])


# part 1
wire1_path = travel(wire1)
wire2_path = travel(wire2)
common = wire1_path.intersection(wire2_path)
print(min(map(norm, common)))