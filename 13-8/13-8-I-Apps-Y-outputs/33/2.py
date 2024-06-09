
def solve(sequences):
    # Initialize variables
    k = len(sequences)
    n = [len(sequence) for sequence in sequences]
    s = [sum(sequence) for sequence in sequences]
    
    # Iterate over all possible pairs of sequences
    for i in range(k):
        for j in range(i+1, k):
            # Check if the sums of the two sequences are equal
            if s[i] == s[j]:
                # Find the index of the element to remove in sequence i
                x = n[i] - 1
                while x > 0 and sequences[i][x] == sequences[j][x]:
                    x -= 1
                # Find the index of the element to remove in sequence j
                y = n[j] - 1
                while y > 0 and sequences[i][x] == sequences[j][y]:
                    y -= 1
                # Check if the indices are valid
                if x > 0 and y > 0:
                    return "YES\n" + str(i+1) + " " + str(x+1) + "\n" + str(j+1) + " " + str(y+1)
    
    return "NO"

