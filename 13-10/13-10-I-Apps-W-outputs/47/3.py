
def get_beauty(arr, k):
    n = len(arr)
    beauty = 0
    for i in range(n - k + 1):
        for j in range(i + 1, n):
            beauty += abs(arr[i] - arr[j])
    return beauty % 998244353

def solve(n, k, arr):
    beauty = 0
    for i in range(n - k + 1):
        beauty += get_beauty(arr[i:i+k], k)
    return beauty % 998244353

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(n, k, arr))

