
def is_k_periodic(arr, k):
    n = len(arr)
    if n % k != 0:
        return False
    b = arr[:k]
    for i in range(n//k):
        if arr[i*k:i*k+k] != b:
            return False
    return True

def min_elements_to_change(arr, k):
    n = len(arr)
    if is_k_periodic(arr, k):
        return 0
    count = 0
    for i in range(n):
        if arr[i] != arr[i%k]:
            count += 1
    return count

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(min_elements_to_change(arr, k))

