
def is_k_periodic(arr, k):
    n = len(arr)
    if n % k != 0:
        return False
    b = arr[:k]
    for i in range(n//k):
        if arr[i*k:i*k+k] != b:
            return False
    return True

def min_changes_to_make_k_periodic(arr, k):
    n = len(arr)
    if is_k_periodic(arr, k):
        return 0
    b = arr[:k]
    count = 0
    for i in range(n//k):
        if arr[i*k:i*k+k] != b:
            count += 1
    return count

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(min_changes_to_make_k_periodic(arr, k))

