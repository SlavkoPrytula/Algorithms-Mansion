ans = []


def solve(arr):
    a = []

    for i in range(len(arr)):
        if i % 2 == 0:
            a.append(arr.pop(0))
        else:
            a.append(arr.pop(-1))

    s = ""
    for i in a:
        s += str(i) + " "

    return s


if __name__ == '__main__':
    k = int(input())
    arr = []
    for i in range(k):
        n = input()
        arr.append([int(x) for x in input().split()])

    for i in range(len(arr)):
        print(solve(arr[i]))
