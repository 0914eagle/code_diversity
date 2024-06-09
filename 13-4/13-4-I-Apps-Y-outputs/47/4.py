
def get_regular_bracket_sequences(n, s):
    # Initialize a list to store the regular bracket sequences
    regular_bracket_sequences = []
    
    # Iterate over all possible bracket sequences of length 2n
    for i in range(2**(2*n)):
        # Convert the binary representation of i to a binary string of length 2n
        binary_string = bin(i)[2:].zfill(2*n)
        
        # Initialize a list to store the current bracket sequence
        current_bracket_sequence = []
        
        # Iterate over the characters of the binary string
        for j in range(len(binary_string)):
            # If the j-th character of the binary string is 1, append a '(' to the current bracket sequence
            if binary_string[j] == '1':
                current_bracket_sequence.append('(')
            # If the j-th character of the binary string is 0, append a ')' to the current bracket sequence
            else:
                current_bracket_sequence.append(')')
                
        # If the current bracket sequence contains s as a substring, add it to the list of regular bracket sequences
        if ''.join(current_bracket_sequence) in s:
            regular_bracket_sequences.append(''.join(current_bracket_sequence))
    
    # Return the list of regular bracket sequences
    return regular_bracket_sequences

def count_regular_bracket_sequences(n, s):
    # Get the list of regular bracket sequences containing s as a substring
    regular_bracket_sequences = get_regular_bracket_sequences(n, s)
    
    # Return the number of regular bracket sequences modulo 1000000007
    return len(regular_bracket_sequences) % 1000000007

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(count_regular_bracket_sequences(n, s))

