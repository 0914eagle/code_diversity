
def solve(sequences):
    # Initialize variables
    n = len(sequences)
    sums = [0] * n
    for i in range(n):
        sums[i] = sum(sequences[i])
    
    # Iterate over all pairs of sequences
    for i in range(n):
        for j in range(i+1, n):
            # Check if the sums of the sequences are equal
            if sums[i] == sums[j]:
                # Find the index of the element to remove in sequence i
                for x in range(len(sequences[i])):
                    if sequences[i][x] != sequences[j][0]:
                        break
                # Find the index of the element to remove in sequence j
                for y in range(len(sequences[j])):
                    if sequences[j][y] != sequences[i][0]:
                        break
                # Return the indices of the elements to remove
                return "YES\n" + str(i+1) + " " + str(x+1) + "\n" + str(j+1) + " " + str(y+1)
    
    # If no pairs of sequences have equal sums, return "NO"
    return "NO"

