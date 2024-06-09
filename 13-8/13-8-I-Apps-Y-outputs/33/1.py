
def solve(sequences):
    # Initialize variables
    n = len(sequences)
    sums = [0] * n
    for i in range(n):
        sums[i] = sum(sequences[i])
    
    # Iterate over all pairs of sequences
    for i in range(n):
        for j in range(i+1, n):
            # Check if the sums of the two sequences are equal
            if sums[i] == sums[j]:
                # Find the indices of the elements to remove
                x = sequences[i].index(max(sequences[i]))
                y = sequences[j].index(max(sequences[j]))
                return "YES\n" + str(i+1) + " " + str(x+1) + "\n" + str(j+1) + " " + str(y+1)
    
    return "NO"

