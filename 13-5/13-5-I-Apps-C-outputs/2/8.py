
def get_input():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return N, a, b

def solve(N, a, b):
    # Initialize the solution with all A's
    solution = ['A'] * N

    # Loop through each candy and check if it should be given to Beata instead
    for i in range(N):
        if b[i] > a[i]:
            solution[i] = 'B'

    return ''.join(solution)

def main():
    N, a, b = get_input()
    print(solve(N, a, b))

if __name__ == '__main__':
    main()

