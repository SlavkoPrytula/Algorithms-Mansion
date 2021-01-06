ans = []


def solve(weights):
    a = []
    b = []
    weights = sorted(weights, key=lambda x: x)[::-1]
    while 1:
        if len(weights) == 0:
            break
        a.append(weights.pop(0))
        while sum(b) != sum(a):
            if len(weights) == 0:
                break
            b.append(weights.pop(0))

    return "YES" if sum(a) == sum(b) else "NO"


if __name__ == '__main__':
    k = int(input())
    arr = []
    for i in range(k):
        n = int(input())
        arr.append([int(x) for x in input().split()])

    for i in range(len(arr)):
        print(solve(arr[i]))
