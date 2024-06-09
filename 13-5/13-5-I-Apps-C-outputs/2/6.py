
def get_input():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return N, a, b

def solve(N, a, b):
    # Initialize the solution with all A's
    solution = ['A'] * N

    # Loop through each candy and check if it can be given to the other sibling
    for i in range(N):
        if a[i] < 0 and b[i] > 0:
            # If the candy is hated by one sibling and loved by the other, give it to the sibling who loves it
            solution[i] = 'B'
        elif a[i] > 0 and b[i] < 0:
            # If the candy is loved by one sibling and hated by the other, give it to the sibling who loves it
            solution[i] = 'A'

    return ''.join(solution)

def main():
    N, a, b = get_input()
    print(solve(N, a, b))

if __name__ == '__main__':
    main()

