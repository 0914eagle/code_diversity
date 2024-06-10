
def get_input():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return N, a, b

def solve(N, a, b):
    # Initialize the solution with all A's
    solution = ['A'] * N

    # Loop through each candy and assign it to the sibling with the highest preference
    for i in range(N):
        if a[i] > b[i]:
            solution[i] = 'B'
        elif a[i] < b[i]:
            solution[i] = 'A'

    return ''.join(solution)

def main():
    N, a, b = get_input()
    print(solve(N, a, b))

if __name__ == '__main__':
    main()

