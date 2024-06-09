
def get_adjacent_replacements(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] += 1
        else:
            arr[i] -= 1
    return arr

def get_final_array(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == 10**9:
            arr[i] = 1
        elif arr[i] == 10**9 - 1:
            arr[i] = 10**9
    return arr

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr = get_adjacent_replacements(arr)
    arr = get_final_array(arr)
    print(*arr)

if __name__ == '__main__':
    main()

