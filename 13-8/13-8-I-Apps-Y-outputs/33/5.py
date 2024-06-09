
def solve(sequences):
    # Initialize variables
    k = len(sequences)
    n_i = []
    a_i = []
    for i in range(k):
        n_i.append(len(sequences[i]))
        a_i.append(sum(sequences[i]))
    
    # Iterate over all possible pairs of sequences
    for i in range(k):
        for j in range(i+1, k):
            # Check if the sums of the sequences are equal
            if a_i[i] == a_i[j]:
                # Find the element to remove in each sequence to make the sum equal
                for x in range(n_i[i]):
                    for y in range(n_i[j]):
                        if sequences[i][x] + sequences[j][y] == a_i[i]:
                            return "YES\n" + str(i+1) + " " + str(x+1) + "\n" + str(j+1) + " " + str(y+1)
    
    return "NO"

