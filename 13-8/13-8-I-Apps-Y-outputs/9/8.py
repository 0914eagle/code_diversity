
def get_maximum_candies(n, k):
    
    # Initialize variables
    min_candies = 0
    max_candies = 0
    total_candies = 0

    # Loop through each possible number of candies for each kid
    for i in range(1, n + 1):
        # Calculate the total number of candies given to kids
        total_candies += i * (k - 1)

        # Check if the total number of candies is less than or equal to the number of candies available
        if total_candies <= n:
            # Update the minimum and maximum number of candies given to each kid
            min_candies = i
            max_candies = i
        # Check if the total number of candies is greater than the number of candies available
        elif total_candies > n:
            # Break the loop
            break

    # Return the maximum number of candies given to each kid
    return max_candies

def main():
    # Read the number of test cases
    t = int(input())

    # Loop through each test case
    for _ in range(t):
        # Read the number of candies and kids
        n, k = map(int, input().split())

        # Find the maximum number of candies Santa can give to kids
        max_candies = get_maximum_candies(n, k)

        # Print the answer
        print(max_candies)

if __name__ == '__main__':
    main()

