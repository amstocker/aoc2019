low = 265275
high = 781584

count_p1 = 0
count_p2 = 0
for n in range(low, high):
    last = ''
    dc = [0] * 10
    for c in str(n):
        dc[int(c)] += 1
        if c < last:
            break
        last = c
    else:
        if any(map(lambda c: c >= 2, dc)):
            count_p1 += 1
        if any(map(lambda c: c == 2, dc)):
            count_p2 += 1

print(count_p1)  # part 1
print(count_p2)  # part 2