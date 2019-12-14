def get_data():
    with open("day2.txt") as f:
        return [int(x) for x in f.read().rstrip().split(',')]

def step(data, cur):
    op = data[cur]
    if op == 99:
        return cur
    src1 = data[cur + 1]
    src2 = data[cur + 2]
    dest = data[cur + 3]
    if op == 1:
        data[dest] = data[src1] + data[src2]
    elif op == 2:
        data[dest] = data[src1] * data[src2]
    else:
        raise RuntimeError
    return cur + 4

def run(data):
    cur = 0
    running = True
    while running:
        last_cur = cur
        cur = step(data, cur)
        if cur == last_cur:
            running = False
    return data[0]


# part 1
data = get_data()
data[1] = 12
data[2] = 2
print(run(data))

# part 2
desired_output = 19690720
data_original = get_data()
for noun in range(100):
    for verb in range(100):
        data = data_original[:]
        data[1] = noun
        data[2] = verb
        if run(data) == desired_output:
            print(100 * noun + verb)
            break