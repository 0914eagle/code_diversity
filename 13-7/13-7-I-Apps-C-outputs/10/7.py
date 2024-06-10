
def get_input():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return N, a, b

def solve(N, a, b):
    # Initialize the solution with all candies given to Alf
    solution = ['A'] * N

    # Loop through each candy and check if it can be given to Beata
    for i in range(N):
        if b[i] > a[i]:
            # If the value of the candy is higher for Beata, give it to her
            solution[i] = 'B'

    return ''.join(solution)

def main():
    N, a, b = get_input()
    print(solve(N, a, b))

if __name__ == '__main__':
    main()

