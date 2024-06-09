
def get_adjacent_replacements(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == 1:
            arr[i] = 2
        elif arr[i] == 2:
            arr[i] = 1
        elif arr[i] == 3:
            arr[i] = 4
        elif arr[i] == 4:
            arr[i] = 3
        elif arr[i] == 5:
            arr[i] = 6
        elif arr[i] == 6:
            arr[i] = 5
        elif arr[i] == 10**9 - 1:
            arr[i] = 10**9
        elif arr[i] == 10**9:
            arr[i] = 10**9 - 1
    return arr

def get_final_array(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == 1:
            arr[i] = 2
        elif arr[i] == 2:
            arr[i] = 1
        elif arr[i] == 3:
            arr[i] = 4
        elif arr[i] == 4:
            arr[i] = 3
        elif arr[i] == 5:
            arr[i] = 6
        elif arr[i] == 6:
            arr[i] = 5
        elif arr[i] == 10**9 - 1:
            arr[i] = 10**9
        elif arr[i] == 10**9:
            arr[i] = 10**9 - 1
    return arr

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(*get_final_array(arr))

