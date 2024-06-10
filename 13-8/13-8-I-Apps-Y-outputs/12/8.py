
def solve(a, k):
    # Initialize variables
    n = len(a)
    x = 0
    moves = 0
    # Loop through each element of the array
    for i in range(n):
        # If the element is not divisible by k, add x to it and increase x by 1
        if a[i] % k != 0:
            a[i] += x
            x += 1
            moves += 1
    # Return the minimum number of moves required to obtain an array where each element is divisible by k
    return moves

def main():
    # Read the input
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        # Call the solve function and print the result
        print(solve(a, k))

if __name__ == '__main__':
    main()

