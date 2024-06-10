
def is_magical(arr):
    return all(arr[0] <= x <= arr[-1] for x in arr)

def solve(arr, l, r):
    sub_arr = arr[l-1:r]
    if is_magical(sub_arr):
        return len(sub_arr)
    else:
        return 0

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        print(solve(arr, l, r))

if __name__ == '__main__':
    main()

