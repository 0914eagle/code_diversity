
def find_triangle(arr):
    n = len(arr)
    for i in range(n - 2):
        lo = i + 1
        hi = n - 1
        while lo < hi:
            p = arr[i]
            q = arr[lo]
            r = arr[hi]
            if p + q > r and p + r > q and q + r > p:
                return [i, lo, hi]
            elif p + q < r or p + r < q or q + r < p:
                lo += 1
            else:
                hi -= 1
    return [-1]

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(*find_triangle(arr))

if __name__ == '__main__':
    main()

