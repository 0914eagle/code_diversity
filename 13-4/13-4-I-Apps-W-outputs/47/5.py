
def f1(n, sequences):
    # f1(n, sequences) returns the maximum number of pairs that can be made from the given bracket sequences
    # n: integer, the number of bracket sequences
    # sequences: list of strings, the bracket sequences
    
    # Initialize a dictionary to store the frequency of each bracket sequence
    freq = {}
    for seq in sequences:
        if seq not in freq:
            freq[seq] = 1
        else:
            freq[seq] += 1
    
    # Initialize a list to store the pairs
    pairs = []
    
    # Iterate through the dictionary and find pairs
    for seq, count in freq.items():
        if count % 2 == 1:
            # If the frequency of the sequence is odd, it cannot be paired
            return len(pairs)
        else:
            # If the frequency of the sequence is even, it can be paired
            pairs.append((seq, seq))
    
    return len(pairs)

def f2(n, sequences):
    # f2(n, sequences) returns the maximum number of pairs that can be made from the given bracket sequences
    # n: integer, the number of bracket sequences
    # sequences: list of strings, the bracket sequences
    
    # Initialize a dictionary to store the frequency of each bracket sequence
    freq = {}
    for seq in sequences:
        if seq not in freq:
            freq[seq] = 1
        else:
            freq[seq] += 1
    
    # Initialize a list to store the pairs
    pairs = []
    
    # Iterate through the dictionary and find pairs
    for seq, count in freq.items():
        if count % 2 == 1:
            # If the frequency of the sequence is odd, it cannot be paired
            return len(pairs)
        else:
            # If the frequency of the sequence is even, it can be paired
            pairs.append((seq, seq))
    
    return len(pairs)

if __name__ == '__main__':
    n = int(input())
    sequences = []
    for _ in range(n):
        sequences.append(input())
    print(f1(n, sequences))
    print(f2(n, sequences))

