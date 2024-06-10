
def get_confused_sequences(N, C):
    # Initialize a list to store the sequences
    sequences = []
    
    # Iterate over all possible sequences
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                # Check if the sequence is valid
                if i != j and i != k and j != k:
                    # Calculate the confusion of the sequence
                    confusion = 0
                    if i > j:
                        confusion += 1
                    if i > k:
                        confusion += 1
                    if j > k:
                        confusion += 1
                    
                    # Check if the confusion is equal to C
                    if confusion == C:
                        # Add the sequence to the list
                        sequences.append([i, j, k])
    
    # Return the number of sequences modulo 1000000007
    return len(sequences) % 1000000007

def main():
    # Read the input
    N, C = map(int, input().split())
    
    # Calculate the number of sequences
    result = get_confused_sequences(N, C)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

