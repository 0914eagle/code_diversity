
def solve(arr, x):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] ^ arr[j] == x:
                count += 1
    return count

