ans = []


def solve(arr):
    arr = sorted(arr, key=lambda x: x[0])
    max_val_x = max([i[0] for i in arr])
    max_val_y = max([i[1] for i in arr])
    max_val = max(max_val_x, max_val_y)

    visited = []

    xs = [i[0] for i in arr]
    ys = [i[1] for i in arr]

    xs.append(max_val + 1)
    res = {}

    # for item in arr:
    #     if item not in visited:
    #         x1 = y1 = min(item[:-2])
    #         x2 = y2 = max(item[:-2])
    #         s = 0
    #         for p in arr:
    #             if (x1 <= p[0] <= x2) and (y1 <= p[1] <= y2):
    #                 s += item[2]
    #                 res.update({s - (x2 - x1): [x1, y1, x2, y2]})

    i = j = min(arr[0][:-2])
    counter = 0
    while i < len(arr) - 1:
        while j < max_val + 2:
            x1 = y1 = i
            x2 = y2 = j
            s = 0
            for item in arr:
                if (x1 <= item[0] <= x2) and (y1 <= item[1] <= y2):
                    s += item[2]
            res.update({s - (x2 - x1): [x1, y1, x2, y2]})
            j += 1
        counter += 1
        i = min(arr[counter][:-2])


    maximum = max(res)
    return maximum, res[maximum]


if __name__ == '__main__':
    k = int(input())
    arr = []
    for _ in range(k):
        arr.append([int(i) for i in input().split()])

    result = solve(arr)
    print(result[0])
    print("".join(str(i) + " " for i in result[1]))
