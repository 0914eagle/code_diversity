
def get_max_earnings(a):
    # Initialize the maximum earnings to 0
    max_earnings = 0
    # Loop through each element in the array
    for i in range(len(a)):
        # Check if the current element is positive
        if a[i] > 0:
            # Add the current element to the maximum earnings
            max_earnings += a[i]
        # Check if the current element is negative
        elif a[i] < 0:
            # Subtract the current element from the maximum earnings
            max_earnings += a[i]
    # Return the maximum earnings
    return max_earnings

def main():
    # Read the number of gems and the values of the gems from stdin
    n = int(input())
    a = list(map(int, input().split()))
    # Call the get_max_earnings function and print the result
    print(get_max_earnings(a))

if __name__ == '__main__':
    main()

