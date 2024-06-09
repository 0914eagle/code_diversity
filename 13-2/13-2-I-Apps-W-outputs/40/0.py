
def get_swaps(arr):
    n = len(arr)
    swaps = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                swaps.append([i, j])
    return swaps

def print_swaps(swaps):
    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    swaps = get_swaps(arr)
    print_swaps(swaps)

