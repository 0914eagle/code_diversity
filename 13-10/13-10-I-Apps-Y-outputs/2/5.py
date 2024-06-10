
def get_max_prettiness(n, a):
    # Sort the prettinesses in descending order
    a.sort(reverse=True)
    # Initialize the maximum prettiness to 0
    max_prettiness = 0
    # Loop through the first three prettinesses
    for i in range(3):
        # Add the current prettiness to the maximum prettiness
        max_prettiness += a[i]
        # If the current prettiness is divisible by the next prettiness, break the loop
        if a[i] % a[i+1] == 0:
            break
    # Return the maximum prettiness
    return max_prettiness

def main():
    # Read the number of queries
    q = int(input())
    # Loop through the queries
    for i in range(q):
        # Read the number of problems and the prettinesses of the problems
        n = int(input())
        a = list(map(int, input().split()))
        # Get the maximum possible prettiness of the contest
        max_prettiness = get_max_prettiness(n, a)
        # Print the maximum possible prettiness
        print(max_prettiness)

if __name__ == '__main__':
    main()

