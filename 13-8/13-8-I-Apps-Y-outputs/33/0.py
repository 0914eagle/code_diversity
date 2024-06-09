
def solve(sequences):
    # Initialize variables
    k = len(sequences)
    n_i = [len(sequence) for sequence in sequences]
    a_i = [sequence for sequence in sequences]
    
    # Loop through each pair of sequences
    for i in range(k):
        for j in range(i+1, k):
            # Check if the lengths of the sequences are equal
            if n_i[i] == n_i[j]:
                # Loop through each element in the first sequence
                for x in range(n_i[i]):
                    # Check if the sum of the elements in the first sequence without the current element is equal to the sum of the elements in the second sequence
                    if sum(a_i[i][:x] + a_i[i][x+1:]) == sum(a_i[j]):
                        return "YES\n" + str(i+1) + " " + str(x+1) + "\n" + str(j+1) + " " + str(n_i[j])
    
    return "NO"

