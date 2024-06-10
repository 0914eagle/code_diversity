
def get_input():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return N, a, b

def solve(N, a, b):
    # Initialize the optimal solution
    opt_sol = [None] * N

    # Loop through each candy
    for i in range(N):
        # If Alf and Beata have the same amount of candy, give it to Alf
        if a[i] == b[i]:
            opt_sol[i] = 'A'
        # If Alf has more candy, give it to Alf
        elif a[i] > b[i]:
            opt_sol[i] = 'A'
        # If Beata has more candy, give it to Beata
        else:
            opt_sol[i] = 'B'

    return ''.join(opt_sol)

def main():
    N, a, b = get_input()
    print(solve(N, a, b))

if __name__ == '__main__':
    main()

