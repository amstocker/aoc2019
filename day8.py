from itertools import chain


W, H = 25, 6

with open("day8.txt") as f:
    data = [int(c) for c in f.read().strip()]

def make_layers(data):
    layers = []
    layer = []
    i = 0
    while i < len(data):
        for y in range(H):
            row = []
            for x in range(W):
                row.append(data[i])
                i += 1
            layer.append(row)
            row = []
        layers.append(layer)
        layer = []
    return layers

def flatten_layer(layer):
    return list(chain(*layer))

def get_min_layer(layers):
    min_count = (W * H) + 1  # max possible value
    min_layer = None
    for layer in layers:
        flattened_layer = flatten_layer(layer)
        count = 0
        for z in flattened_layer:
            if z == 0:
                count += 1
        if count < min_count:
            min_count = count
            min_layer = layer
    return min_layer

def answer_from_layer(layer):
    flattened_layer = flatten_layer(layer)
    ones_sum = 0
    twos_sum = 0
    for z in flattened_layer:
        if z == 1:
            ones_sum += 1
        if z == 2:
            twos_sum += 1
    return ones_sum * twos_sum


# part 1
layers = make_layers(data)
min_layer = get_min_layer(layers)
print(answer_from_layer(min_layer))