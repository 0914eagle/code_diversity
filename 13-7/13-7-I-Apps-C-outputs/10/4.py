
def get_input():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return N, a, b

def solve(N, a, b):
    # Initialize the optimal solution
    opt = [0] * N
    
    # Loop through each candy
    for i in range(N):
        # If Alf prefers the current candy
        if a[i] > b[i]:
            # Give the candy to Alf
            opt[i] = 'A'
        # If Beata prefers the current candy
        elif a[i] < b[i]:
            # Give the candy to Beata
            opt[i] = 'B'
        # If the candy is indifferent
        else:
            # Give the candy to Alf if it is even, and to Beata if it is odd
            opt[i] = 'A' if i % 2 == 0 else 'B'
    
    return ''.join(opt)

def main():
    N, a, b = get_input()
    print(solve(N, a, b))

if __name__ == '__main__':
    main()

