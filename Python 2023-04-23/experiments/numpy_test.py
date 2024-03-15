import numpy as np

map = np.random.randint(0, 10, (4, 4))


print(map)
print(map.shape)
x_len, y_len = map.shape
size = 2
scan_end = int(size / 2)

for x in range(x_len-scan_end):
    for y in range(y_len-scan_end):
        x_min = x
        y_min = y
        x_max = x + size
        y_max = y + size

        arr = map[x_min:x_max, y_min:y_max]
        diff = arr.max() - arr.min()
        std = arr.std()
        print(arr)
        print(
            f'x: ({x_min},{x_max}), y: ({y_min}, {y_max}) -> height_diff {diff} , std: {std}')
        print()
