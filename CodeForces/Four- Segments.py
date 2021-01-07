ans = []

def solve(arr):
    arr = sorted(arr, key=lambda x: x)
    return arr[0] * arr[2]


if __name__ == '__main__':
    k = int(input())
    arr = []
    for i in range(k):
        arr.append([int(x) for x in input().split()])

    for i in range(len(arr)):
        print(solve(arr[i]))
