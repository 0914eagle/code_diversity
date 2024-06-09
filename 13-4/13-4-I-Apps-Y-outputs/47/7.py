
def f1(n, s):
    # Initialize the number of regular bracket sequences as 0
    num_seq = 0
    
    # Loop through all possible combinations of '(' and ')' with length 2n
    for comb in itertools.product('()', repeat=2*n):
        # Check if the current combination is a regular bracket sequence
        if is_regular_sequence(comb):
            # Check if the current sequence contains the given bracket sequence as a substring
            if s in ''.join(comb):
                # Increment the number of regular bracket sequences
                num_seq += 1
    
    # Return the number of regular bracket sequences modulo 10^9+7
    return num_seq % 1000000007

def is_regular_sequence(seq):
    # Initialize the number of open brackets as 0
    num_open = 0
    
    # Loop through the characters in the sequence
    for char in seq:
        # If the current character is '('
        if char == '(':
            # Increment the number of open brackets
            num_open += 1
        # If the current character is ')'
        elif char == ')':
            # Decrement the number of open brackets
            num_open -= 1
            # If the number of open brackets becomes negative, the sequence is not regular
            if num_open < 0:
                return False
    
    # If the number of open brackets is not 0 at the end of the sequence, the sequence is not regular
    if num_open != 0:
        return False
    
    # The sequence is regular
    return True

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(f1(n, s))

