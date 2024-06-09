
def f1(n, arr):
    # Replace all occurrences of 1 with 2
    for i in range(n):
        if arr[i] == 1:
            arr[i] = 2
    return arr

def f2(n, arr):
    # Replace all occurrences of 2 with 1
    for i in range(n):
        if arr[i] == 2:
            arr[i] = 1
    return arr

def f3(n, arr):
    # Replace all occurrences of 3 with 4
    for i in range(n):
        if arr[i] == 3:
            arr[i] = 4
    return arr

def f4(n, arr):
    # Replace all occurrences of 4 with 3
    for i in range(n):
        if arr[i] == 4:
            arr[i] = 3
    return arr

def f5(n, arr):
    # Replace all occurrences of 5 with 6
    for i in range(n):
        if arr[i] == 5:
            arr[i] = 6
    return arr

def f6(n, arr):
    # Replace all occurrences of 6 with 5
    for i in range(n):
        if arr[i] == 6:
            arr[i] = 5
    return arr

def f7(n, arr):
    # Replace all occurrences of 10 with 9
    for i in range(n):
        if arr[i] == 10:
            arr[i] = 9
    return arr

def apply_algorithm(n, arr):
    # Apply the algorithm to the array
    for i in range(n):
        if arr[i] == 1:
            arr = f1(n, arr)
        elif arr[i] == 2:
            arr = f2(n, arr)
        elif arr[i] == 3:
            arr = f3(n, arr)
        elif arr[i] == 4:
            arr = f4(n, arr)
        elif arr[i] == 5:
            arr = f5(n, arr)
        elif arr[i] == 6:
            arr = f6(n, arr)
        elif arr[i] == 10:
            arr = f7(n, arr)
    return arr

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = apply_algorithm(n, arr)
    print(*result)

