ans = []


def solve(arr):
    # ways = []
    # for i in range(len(arr)):
    #     j = i
    #     way = 0
    #     while j < len(arr):
    #         way += arr[j]
    #         j += arr[j]
    #     ways.append(way)
    # return max(ways)

    new_arr = [[i, 0] for i in arr]
    for i in range(len(new_arr) - 1, -1, -1):
        if new_arr[i][0] + i < len(new_arr):
            new_arr[i][1] += new_arr[new_arr[i][0] + i][1] + new_arr[i][0]
        else:
            new_arr[i][1] += new_arr[i][0]

    return max([i[1] for i in new_arr])


if __name__ == '__main__':
    k = int(input())
    arr = []
    for i in range(k):
        n = int(input())
        arr.append([int(x) for x in input().split()])

    for i in range(len(arr)):
        print(solve(arr[i]))
