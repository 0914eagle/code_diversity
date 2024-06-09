
def get_mex(arr):
    mex = 0
    for i in range(len(arr)):
        if arr[i] > mex:
            mex = arr[i]
    return mex + 1

def get_strength(arr):
    return get_mex(arr)

def get_max_strength(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = get_strength(arr[:i])
    max_strength = 0
    for i in range(k):
        max_strength = max(max_strength, dp[i])
    return max_strength

def main():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = int(input())
    k = list(map(int, input().split()))
    print(get_max_strength(p, d))

if __name__ == '__main__':
    main()

