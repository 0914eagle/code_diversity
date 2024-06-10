
def can_reach_n_from_0(n, m, d, c):
    # Initialize the array a
    a = [0] * (n + 2)
    # Set the cells belonging to the first platform
    a[1:c[0] + 1] = [1] * c[0]
    # Iterate over the remaining platforms
    for i in range(1, m):
        # Set the cells belonging to the current platform
        a[c[i - 1] + 1:c[i] + c[i - 1] + 1] = [i + 1] * c[i]
        # Update the maximum distance of jump
        d = max(d, c[i])
    # Check if it is possible to reach n + 1 from 0
    if a[n + 1] == 0:
        return "NO"
    else:
        return "YES"
        # Return the array a
        return a

def main():
    # Read the input
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    # Call the can_reach_n_from_0 function
    result = can_reach_n_from_0(n, m, d, c)
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

