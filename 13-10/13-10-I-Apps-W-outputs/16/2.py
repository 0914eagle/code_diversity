
def find_smallest_sum(k):
    # Initialize a list to store the possible multiples of k
    multiples = []
    
    # Iterate from 1 to 10^5
    for i in range(1, 100001):
        # Check if i is a multiple of k
        if i % k == 0:
            # Add the decimal representation of i to the list
            multiples.append(str(i))
    
    # Initialize a variable to store the smallest sum
    smallest_sum = float('inf')
    
    # Iterate through the list of possible multiples
    for multiple in multiples:
        # Calculate the sum of the digits in the decimal representation of the multiple
        sum_of_digits = sum([int(digit) for digit in multiple])
        
        # Check if the sum is smaller than the current smallest sum
        if sum_of_digits < smallest_sum:
            # Update the smallest sum
            smallest_sum = sum_of_digits
    
    # Return the smallest sum
    return smallest_sum

def main():
    # Read a line of input from stdin and convert it to an integer
    k = int(input().strip())
    
    # Print the smallest possible sum of the digits in the decimal notation of a positive multiple of k
    print(find_smallest_sum(k))

if __name__ == '__main__':
    main()

