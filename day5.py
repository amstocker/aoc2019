# Air conditioner ID number
ID = 1

def get_data():
    with open("day5.txt") as f:
        return [int(x) for x in f.read().rstrip().split(',')]

def step_v1(data, cur):
    inst = data[cur]
    op = inst % 100
    if op == 99:
        return cur
    arg1 = data[cur + 1]
    arg2 = data[cur + 2]
    dest = data[cur + 3]
    val1 = arg1 if (inst // 100) % 10 else data[arg1]
    if op < 3:
        val2 = arg2 if (inst // 1000) % 10 else data[arg2]
    else:
        val2 = None
    if op == 1:
        data[dest] = val1 + val2
        return cur + 4
    elif op == 2:
        data[dest] = val1 * val2
        return cur + 4
    elif op == 3:
        data[arg1] = ID
        return cur + 2
    elif op == 4:
        print("Output:", val1)
        return cur + 2
    else:
        raise RuntimeError

def run(data, step=step_v1):
    cur = 0
    running = True
    while running:
        last_cur = cur
        cur = step(data, cur)
        if cur == last_cur:
            running = False
    return data[0]


# part 1
run(get_data())