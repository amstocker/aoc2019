# Password length
N = 6

# Represent passwords as lists of integers
low = list(map(int, str(265275)))
high = list(map(int, str(781584)))

def make_password(password, start, depth):
    if depth >= N:
        yield password
    else:
        for n in range(start, 10):
            yield from make_password(password[:] + [n], n, depth + 1)

# Generate non-decreasing passwords and check for doubles.
counter_p1 = 0
counter_p2 = 0
for pw in make_password([], 0, 0):
    if low <= pw <= high:
        digit_count = 10 * [0]
        for n in pw:
            digit_count[n] += 1
        if any(map(lambda n: n >= 2, digit_count)):
            counter_p1 += 1
        if any(map(lambda n: n == 2, digit_count)):
            counter_p2 += 1

print(counter_p1)  # part 1
print(counter_p2)  # part 2