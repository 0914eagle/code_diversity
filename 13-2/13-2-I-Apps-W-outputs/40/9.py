
def get_swaps(arr):
    n = len(arr)
    swaps = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                swaps.append([i, j])
    return swaps

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    swaps = get_swaps(arr)
    print(len(swaps))
    for swap in swaps:
        print(*swap)

if __name__ == '__main__':
    main()

