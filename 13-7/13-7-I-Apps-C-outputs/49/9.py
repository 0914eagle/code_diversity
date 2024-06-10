
def get_input():
    N, M = map(int, input().split())
    permutation = list(map(int, input().split()))
    swaps = []
    for i in range(M):
        a, b = map(int, input().split())
        swaps.append((a, b))
    return N, M, permutation, swaps

def solve(N, M, permutation, swaps):
    # Your code here
    pass

def main():
    N, M, permutation, swaps = get_input()
    result = solve(N, M, permutation, swaps)
    print(result)

if __name__ == '__main__':
    main()

