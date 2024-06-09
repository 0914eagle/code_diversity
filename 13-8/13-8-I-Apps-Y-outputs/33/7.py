
def solve(sequences):
    # Initialize variables
    k = len(sequences)
    n_i = [len(sequence) for sequence in sequences]
    a_i = [[element for element in sequence] for sequence in sequences]
    
    # Iterate over all possible pairs of sequences
    for i in range(k):
        for j in range(i+1, k):
            # Check if the sums of the sequences are equal
            if sum(a_i[i]) == sum(a_i[j]):
                # Find the indices of the elements to remove
                x = a_i[i].index(min(a_i[i]))
                y = a_i[j].index(min(a_i[j]))
                return "YES\n" + str(i+1) + " " + str(x+1) + "\n" + str(j+1) + " " + str(y+1)
    
    return "NO"

