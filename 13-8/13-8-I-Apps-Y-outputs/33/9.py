
def solve(sequences):
    # Initialize variables
    k = len(sequences)
    n_i = [len(sequence) for sequence in sequences]
    a_i = [sum(sequence) for sequence in sequences]
    b_i = [0] * k
    c_i = [0] * k

    # Loop through each sequence
    for i in range(k):
        # Loop through each element in the sequence
        for x in range(n_i[i]):
            # Calculate the sum of the sequence without the current element
            b_i[i] = a_i[i] - sequences[i][x]
            # Check if the sum is equal to the sum of any other sequence
            for j in range(k):
                if i != j and b_i[i] == a_i[j]:
                    # If it is, return the indices of the sequences and the element to remove
                    return "YES\n" + str(i+1) + " " + str(x+1) + "\n" + str(j+1) + " " + str(n_i[j]-1)

    # If no matching sequences are found, return "NO"
    return "NO"

