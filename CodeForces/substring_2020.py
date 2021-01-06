ans = []


def solve(string):
    n = len(string)
    # great = string.find("2020")
    # if great != -1:
    #     if great == 0 or great + 4 == len(string):
    #         return "YES"
    #     else:
    #         return "NO"

    if string[0:2] == "20" and string[n - 2:n] == "20":
        return "YES"
    elif string[0:3] == "202" and string[n - 1:n] == "0":
        return "YES"
    elif string[0:1] == "2" and string[n - 3:n] == "020":
        return "YES"
    elif string[0:4] == "2020" or string[n-4:n] == "2020":
        return "YES"
    else:
        return "NO"

    # while 1:
    #     index = string.find("20")
    #     if index == -1:
    #         return "NO"
    #
    #     new_index = string[index + 2:].find("20")
    #     if new_index == -1:
    #         return "NO"
    #
    #     if new_index + 2 == len(string[index + 2:]):
    #         return "YES"
    #     else:
    #         return "NO"


if __name__ == '__main__':
    k = int(input())
    arr = []
    for i in range(k):
        n = input()
        arr.append(str(input()))

    for i in range(len(arr)):
        print(solve(arr[i]))
