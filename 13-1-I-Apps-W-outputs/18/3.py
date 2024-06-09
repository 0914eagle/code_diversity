
def get_good_sequences(n, a):
    # Initialize a set to store the good sequences
    good_sequences = set()
    
    # Iterate over each possible length of the sequence
    for length in range(1, n + 1):
        # Iterate over each possible starting index of the sequence
        for start in range(n - length + 1):
            # Get the end index of the sequence
            end = start + length - 1
            
            # Check if the sequence is good
            if is_good_sequence(a[start:end+1]):
                # Add the sequence to the set of good sequences
                good_sequences.add((start, end))
    
    # Return the number of good sequences
    return len(good_sequences)

def is_good_sequence(sequence):
    # Initialize a variable to store the result
    result = True
    
    # Iterate over each number in the sequence
    for i in range(len(sequence)):
        # Get the current number and its binary representation
        num = sequence[i]
        binary = bin(num)[2:]
        
        # Iterate over each bit in the binary representation
        for j in range(len(binary)):
            # Check if the bit is set
            if binary[j] == "1":
                # Get the index of the bit
                bit_index = len(binary) - j - 1
                
                # Check if the bit is set in any of the previous numbers
                for k in range(i):
                    # Get the previous number and its binary representation
                    prev_num = sequence[k]
                    prev_binary = bin(prev_num)[2:]
                    
                    # Check if the bit is set in the previous number
                    if prev_binary[bit_index] == "1":
                        # The sequence is not good
                        result = False
                        break
    
    # Return the result
    return result

