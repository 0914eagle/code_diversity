
def get_min_operations(arr):
    n = len(arr)
    count = 0
    for i in range(n-1):
        if arr[i] != arr[i+1]:
            count += 1
    return count

def solve(n, arr):
    min_operations = get_min_operations(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] != arr[j]:
                continue
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            min_operations = min(min_operations, get_min_operations(arr))
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
    return min_operations

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n, arr))

