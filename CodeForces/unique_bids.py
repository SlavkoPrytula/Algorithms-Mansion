ans = []

def solve(arr):
    bids = {}
    first = arr[0]
    for i in arr:
        if i not in bids:
            bids[i] = 1
        else:
            bids[i] += 1

    res = []
    for j in bids:
        if bids[j] == 1:
            res.append(j)

    if not res:
        return -1
    value = min(res)
    return arr.index(value) + 1


if __name__ == '__main__':
    k = int(input())
    arr = []
    for i in range(k):
        n = input()
        arr.append([int(x) for x in input().split()])

    for i in range(len(arr)):
        print(solve(arr[i]))
