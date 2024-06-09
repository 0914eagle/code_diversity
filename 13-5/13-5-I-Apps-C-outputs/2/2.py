
def get_input():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return N, a, b

def solve(N, a, b):
    # Initialize the solution with all A's
    solution = ['A'] * N

    # Loop through the candies and find the best assignment for each one
    for i in range(N):
        # If Alf prefers the current candy to Beata
        if a[i] > b[i]:
            # Assign the candy to Alf
            solution[i] = 'A'
        # If Beata prefers the current candy to Alf
        elif b[i] > a[i]:
            # Assign the candy to Beata
            solution[i] = 'B'

    return ''.join(solution)

def main():
    N, a, b = get_input()
    print(solve(N, a, b))

if __name__ == '__main__':
    main()

