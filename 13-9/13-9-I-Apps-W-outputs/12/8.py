
def input_permutation():
    n = int(input())
    permutation = list(map(int, input().split()))
    return n, permutation

def sort_permutation(permutation):
    n = len(permutation)
    swaps = []
    for i in range(n):
        for j in range(i+1, n):
            if abs(permutation[i] - permutation[j]) >= n//2:
                swaps.append((i, j))
                permutation[i], permutation[j] = permutation[j], permutation[i]
    return permutation, swaps

def output_swaps(swaps):
    print(len(swaps))
    for i, j in swaps:
        print(i+1, j+1)

if __name__ == '__main__':
    n, permutation = input_permutation()
    sorted_permutation, swaps = sort_permutation(permutation)
    output_swaps(swaps)

