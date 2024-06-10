
def sort_permutation(permutation):
    n = len(permutation)
    swaps = []
    for i in range(n):
        for j in range(i+1, n):
            if abs(permutation[i] - permutation[j]) >= n//2:
                swaps.append([i, j])
                break
    return swaps

def get_sorted_permutation(permutation, swaps):
    sorted_permutation = permutation[:]
    for swap in swaps:
        sorted_permutation[swap[0]], sorted_permutation[swap[1]] = sorted_permutation[swap[1]], sorted_permutation[swap[0]]
    return sorted_permutation

def main():
    n = int(input())
    permutation = list(map(int, input().split()))
    swaps = sort_permutation(permutation)
    print(len(swaps))
    for swap in swaps:
        print(*swap)

if __name__ == '__main__':
    main()

