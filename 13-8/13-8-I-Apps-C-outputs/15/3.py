
def get_entirely_unsorted_sequences(numbers):
    # Initialize a set to store the sorted sequences
    sorted_sequences = set()
    
    # Iterate over the input numbers
    for i in range(len(numbers)):
        # Get the current number
        current_number = numbers[i]
        
        # Initialize a set to store the unsorted sequences for the current number
        unsorted_sequences = set()
        
        # Iterate over the remaining numbers
        for j in range(i+1, len(numbers)):
            # Get the next number
            next_number = numbers[j]
            
            # If the current number is less than the next number, add the current number to the unsorted sequence
            if current_number < next_number:
                unsorted_sequences.add((current_number,))
            
            # If the current number is greater than the next number, add the next number to the unsorted sequence
            elif current_number > next_number:
                unsorted_sequences.add((next_number,))
            
            # If the current number is equal to the next number, add both numbers to the unsorted sequence
            else:
                unsorted_sequences.add((current_number, next_number))
        
        # Add the unsorted sequences for the current number to the sorted sequences
        sorted_sequences |= unsorted_sequences
    
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

