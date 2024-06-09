
def get_common_divisors(arr):
    # Initialize a set to store the common divisors
    common_divisors = set()

    # Iterate over the array
    for i in range(len(arr)):
        # Get the current number
        num = arr[i]

        # Iterate over the previous numbers
        for j in range(i):
            # Check if the current number is divisible by the previous number
            if num % arr[j] == 0:
                # Add the previous number to the set of common divisors
                common_divisors.add(arr[j])

    # Return the length of the set of common divisors
    return len(common_divisors)

def main():
    # Read the input array
    n = int(input())
    arr = list(map(int, input().split()))

    # Call the function to get the number of common divisors
    result = get_common_divisors(arr)

    # Print the result
    print(result)

if __name__ == '__main__':
    main()

