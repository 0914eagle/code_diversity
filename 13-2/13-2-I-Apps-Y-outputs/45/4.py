
def get_common_divisors(arr):
    # Initialize a set to store the common divisors
    common_divisors = set()
    
    # Iterate through the array
    for i in range(len(arr)):
        # Get the current number
        num = arr[i]
        
        # Initialize a set to store the divisors of the current number
        divisors = set()
        
        # Iterate through the range of the current number
        for j in range(1, num + 1):
            # If the current number is divisible by j, add j to the set of divisors
            if num % j == 0:
                divisors.add(j)
        
        # If this is the first number, set the common divisors to the set of divisors
        if i == 0:
            common_divisors = divisors
        # Otherwise, find the intersection of the common divisors and the set of divisors
        else:
            common_divisors &= divisors
    
    # Return the number of elements in the set of common divisors
    return len(common_divisors)

def main():
    # Read the input array
    n = int(input())
    arr = [int(x) for x in input().split()]
    
    # Call the function to get the number of common divisors
    result = get_common_divisors(arr)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

