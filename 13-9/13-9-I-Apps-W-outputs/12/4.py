
def read_input():
    n = int(input())
    p = list(map(int, input().split()))
    return n, p

def sort_permutation(n, p):
    swaps = []
    for i in range(n):
        for j in range(i+1, n):
            if abs(i-j) >= n//2:
                swaps.append((i, j))
                break
    return swaps

def print_output(swaps):
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == '__main__':
    n, p = read_input()
    swaps = sort_permutation(n, p)
    print_output(swaps)

