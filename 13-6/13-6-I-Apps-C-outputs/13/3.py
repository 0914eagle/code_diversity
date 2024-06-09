
def get_entirely_unsorted_sequences(arr):
    n = len(arr)
    count = 0
    for i in range(1, n + 1):
        for perm in permutations(arr, i):
            if not is_sorted(perm):
                count += 1
    return count % (10**9 + 9)

def is_sorted(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j] and arr[j] != arr[i]:
                return False
    return True

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_entirely_unsorted_sequences(arr))

