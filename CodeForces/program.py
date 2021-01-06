def read():
    k = int(input())
    arr = []
    for i in range(k):
        arr.append([int(x) for x in input().split()])
    return k, arr


ans = []


def solve(w, h, n):
    cuts = 0
    while w % 2 == 0 or h % 2 == 0:
        if w % 2 == 0:
            w /= 2
        elif h % 2 == 0:
            h /= 2
        cuts += 1

    if 2**cuts >= n:
        return "YES"
    return "NO"


if __name__ == '__main__':
    k, arr = read()
    for i in range(k):
        print(solve(arr[i][0], arr[i][1], arr[i][2]))
