
def solve(sequences):
    # Initialize variables
    k = len(sequences)
    sums = [0] * k
    for i in range(k):
        sums[i] = sum(sequences[i])
    
    # Iterate over all pairs of sequences
    for i in range(k):
        for j in range(i+1, k):
            # Check if the sums of the two sequences are equal
            if sums[i] == sums[j]:
                # Find the element to remove in the first sequence
                for x in range(len(sequences[i])):
                    if sequences[i][x] not in sequences[j]:
                        break
                # Find the element to remove in the second sequence
                for y in range(len(sequences[j])):
                    if sequences[j][y] not in sequences[i]:
                        break
                # Check if the elements are not equal
                if x != y:
                    return "YES\n" + str(i+1) + " " + str(x+1) + "\n" + str(j+1) + " " + str(y+1)
    
    return "NO"

