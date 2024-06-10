
def get_maximum_candies(n, k):
    # Initialize variables
    min_candies = 0
    max_candies = 0
    total_candies = 0

    # Loop through each possible number of candies for each kid
    for i in range(1, n + 1):
        # Calculate the total number of candies given to kids with i candies
        total_candies += i * (k // i)

        # If the total number of candies is greater than the maximum number of candies, update the maximum number of candies
        if total_candies > max_candies:
            max_candies = total_candies

        # If the total number of candies is less than the minimum number of candies, update the minimum number of candies
        if total_candies < min_candies:
            min_candies = total_candies

    # Return the maximum number of candies that Santa can give to kids so that he will be satisfied
    return max_candies

def main():
    # Read the number of test cases
    t = int(input())

    # Loop through each test case
    for _ in range(t):
        # Read the number of candies and kids
        n, k = map(int, input().split())

        # Call the get_maximum_candies function and print the result
        print(get_maximum_candies(n, k))

if __name__ == '__main__':
    main()

