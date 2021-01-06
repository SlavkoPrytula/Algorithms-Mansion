ans = []


def solve(arr):
    x, y = 0, 0
    move = 0
    cur_move_n = 0
    cur_move_e = 0
    cur_move_w = 0
    cur_move_s = 0
    while x != arr[0] or y != arr[1]:
        if x < arr[0] and cur_move_e < 2:
            print("e")
            if cur_move_n == 2 or cur_move_w == 2 or cur_move_s == 2:
                cur_move_n = 0
                cur_move_w = 0
                cur_move_s = 0
            x += 1
            cur_move_e += 1
        elif x > arr[0] and cur_move_w < 2:
            print("w")
            if cur_move_n == 2 or cur_move_e == 2 or cur_move_s == 2:
                cur_move_n = 0
                cur_move_e = 0
                cur_move_s = 0
            x -= 1
            cur_move_w += 1

        elif y < arr[1] and cur_move_n < 2:
            print("n")
            if cur_move_e == 2 or cur_move_w == 2 or cur_move_s == 2:
                cur_move_e = 0
                cur_move_w = 0
                cur_move_s = 0
            y += 1
            cur_move_n += 1
        elif y > arr[1] and cur_move_s < 2:
            print("s")
            if cur_move_n == 2 or cur_move_w == 2 or cur_move_e == 2:
                cur_move_n = 0
                cur_move_e = 0
                cur_move_w = 0
            y -= 1
            cur_move_s += 1
        else:
            print("0")
            cur_move_n = 0
            cur_move_e = 0
            cur_move_w = 0
            cur_move_s = 0

        move += 1

    return move


if __name__ == '__main__':
    k = int(input())
    arr = []
    for i in range(k):
        arr.append([int(x) for x in input().split()])

    for i in range(len(arr)):
        print(solve(arr[i]))
