
def read_input():
    n = int(input())
    p = list(map(int, input().split()))
    return n, p

def solve(n, p):
    # Initialize the number of swaps to 0
    m = 0
    # Initialize the array of swaps to be performed
    swaps = []
    # Loop through the array and find pairs of indices that are at least n/2 apart
    for i in range(n):
        for j in range(i+1, n):
            # If the difference between the indices is at least n/2, add the indices to the array of swaps
            if abs(i-j) >= n//2:
                swaps.append((i, j))
                m += 1
    # If the number of swaps is greater than 5n, return -1 to indicate that it is not possible to sort the array
    if m > 5*n:
        return -1
    # Otherwise, return the array of swaps
    return swaps

def print_output(swaps):
    # If the array of swaps is empty, print 0
    if not swaps:
        print(0)
    # Otherwise, print the number of swaps and the indices to be swapped
    else:
        print(len(swaps))
        for i, j in swaps:
            print(i, j)

if __name__ == '__main__':
    n, p = read_input()
    swaps = solve(n, p)
    print_output(swaps)

