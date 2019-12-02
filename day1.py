def mass_to_fuel(m):
    return max((m // 3) - 2, 0)

def total_fuel(m):
    total = 0
    while m > 0:
        m = mass_to_fuel(m)
        total += m
    return total

with open("day1.txt") as f:
    data = [int(l) for l in f.read().rstrip().split('\n')]

# part 1
print(sum(mass_to_fuel(m) for m in data))

# part 2
print(sum(total_fuel(m) for m in data))