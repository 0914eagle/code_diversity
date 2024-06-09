
def get_mex(subset):
    mex = 0
    for i in range(1, len(subset) + 1):
        if i not in subset:
            mex = i
            break
    return mex


def solve(n, arr):
    arr.sort()
    i, j = 0, 0
    while i < n and j < n:
        if arr[i] == arr[j]:
            j += 1
        else:
            i += 1
            j = i
    A = arr[:i]
    B = arr[i:]
    return get_mex(A) + get_mex(B)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(n, arr))

