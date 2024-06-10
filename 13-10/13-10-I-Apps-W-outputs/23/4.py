
def max_candies(n, k, M, D):
    # Initialize the maximum number of candies as 0
    max_candies = 0
    # Loop through all possible values of x
    for x in range(1, min(n, 1000) + 1):
        # Check if x is a valid value of x
        if x <= M and n % x == 0:
            # Calculate the number of candies each person will receive
            candies_per_person = n // x
            # Calculate the number of times each person will receive candies
            times_each_person_receives = k // candies_per_person
            # Check if no person receives candies more than D times
            if times_each_person_receives <= D:
                # Update the maximum number of candies if necessary
                max_candies = max(max_candies, candies_per_person)
    # Return the maximum number of candies
    return max_candies

def main():
    # Read the input
    n, k, M, D = map(int, input().split())
    # Call the max_candies function and print the result
    print(max_candies(n, k, M, D))

if __name__ == '__main__':
    main()

