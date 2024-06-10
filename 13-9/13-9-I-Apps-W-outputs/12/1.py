
def get_sorted_permutation(permutation):
    n = len(permutation)
    swaps = []
    for i in range(n):
        for j in range(i+1, n):
            if abs(i-j) >= n//2:
                swaps.append((i, j))
                break
    return swaps

def perform_swaps(permutation, swaps):
    for i, j in swaps:
        permutation[i], permutation[j] = permutation[j], permutation[i]
    return permutation

if __name__ == '__main__':
    n = int(input())
    permutation = list(map(int, input().split()))
    swaps = get_sorted_permutation(permutation)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    permutation = perform_swaps(permutation, swaps)
    print(*permutation)

