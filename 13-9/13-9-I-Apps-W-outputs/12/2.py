
def get_sorted_permutation(p):
    n = len(p)
    swaps = []
    for i in range(n):
        for j in range(i+1, n):
            if abs(i-j) >= n//2:
                swaps.append((i, j))
                break
    return swaps

def print_swaps(swaps):
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))
    swaps = get_sorted_permutation(p)
    print_swaps(swaps)

