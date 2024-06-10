
def read_input():
    N, M = map(int, input().split())
    permutation = list(map(int, input().split()))
    swaps = []
    for _ in range(M):
        a, b = map(int, input().split())
        swaps.append((a, b))
    return N, M, permutation, swaps

def solve(N, M, permutation, swaps):
    # implement your solution here
    pass

def main():
    N, M, permutation, swaps = read_input()
    result = solve(N, M, permutation, swaps)
    print(result)

if __name__ == '__main__':
    main()

