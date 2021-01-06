ans = []


def solve(arr):
    al = 0
    bob = 0
    turn = 0
    arr = sorted(arr, reverse=True)
    i = 0
    while i != len(arr):
        if turn % 2 == 0:
            val = arr[i]
            if val % 2 == 0:
                al += val
        else:
            val = arr[i]
            if val % 2 == 1:
                bob += val
        turn ^= 1
        i += 1

    # while odds or even:
    #     if turn % 2 == 0:
    #         if (sum(odds) <= sum(even)) and even != []:
    #             item = max(even)
    #             even.remove(item)
    #             al += item
    #         elif sum(odds) > sum(even) and odds != []:
    #             odds.remove(max(odds))
    #
    #     else:
    #         if (sum(odds) >= sum(even)) and odds != []:
    #             item = max(odds)
    #             odds.remove(item)
    #             bob += item
    #         elif sum(odds) < sum(even) and even != []:
    #             even.remove(max(even))
    #     turn += 1

    if bob > al:
        return "Bob"
    elif bob < al:
        return "Alice"
    else:
        return "Tie"


if __name__ == '__main__':
    k = int(input())
    arr = []
    for i in range(k):
        n = int(input())
        arr.append([int(x) for x in input().split()])

    for i in range(len(arr)):
        print(solve(arr[i]))
