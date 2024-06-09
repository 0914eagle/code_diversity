
import sys

def get_entirely_unsorted_sequences(numbers):
    # Initialize a set to store the sorted sequences
    sorted_sequences = set()
    
    # Iterate over the input numbers
    for i in range(len(numbers)):
        # Get the current number
        current_number = numbers[i]
        
        # Iterate over the remaining numbers
        for j in range(i+1, len(numbers)):
            # Get the next number
            next_number = numbers[j]
            
            # Check if the current number is less than the next number
            if current_number < next_number:
                # If so, add the sorted sequence to the set
                sorted_sequences.add(tuple(numbers[i:j+1]))
    
    # Return the number of sorted sequences
    return len(sorted_sequences)

def main():
    # Read the input
    n = int(input())
    numbers = tuple(map(int, input().split()))
    
    # Call the function to get the number of entirely unsorted sequences
    result = get_entirely_unsorted_sequences(numbers)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

