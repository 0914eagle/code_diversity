
def f1(n, s):
    # Calculate the number of regular bracket sequences of length 2n
    # containing the given bracket sequence s as a substring
    num_sequences = 0
    
    # Iterate over all possible positions of s in a regular bracket sequence
    for i in range(n - len(s) + 1):
        # Check if s is a substring of the regular bracket sequence
        if s in generate_sequence(n, i):
            num_sequences += 1
    
    return num_sequences % 1000000007

def generate_sequence(n, i):
    # Generate all possible regular bracket sequences of length 2n
    sequences = []
    
    # Iterate over all possible positions of '(' and ')' in the sequence
    for j in range(2**n):
        sequence = ""
        for k in range(n):
            if j & (1 << k):
                sequence += "("
            else:
                sequence += ")"
        sequences.append(sequence)
    
    return sequences

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(f1(n, s))

