
def solve(sequences):
    # Initialize variables
    k = len(sequences)
    n_i = []
    n_j = []
    x = 0
    y = 0
    
    # Iterate over the sequences
    for i in range(k):
        # Get the length of the current sequence
        n_i.append(len(sequences[i]))
        # Iterate over the elements of the current sequence
        for j in range(n_i[i]):
            # If the element is not the last one
            if j < n_i[i] - 1:
                # Check if the sum of the elements of the current sequence without the current element is equal to the sum of the elements of the current sequence without the last element
                if sum(sequences[i][:j]) + sum(sequences[i][j+1:]) == sum(sequences[i]):
                    # If it is, set the index of the element to remove and the index of the sequence
                    x = j
                    y = i
                    break
    
    # Check if a solution has been found
    if x == 0 and y == 0:
        return "NO"
    else:
        return "YES\n" + str(y) + " " + str(x) + "\n" + str(i) + " " + str(y)

