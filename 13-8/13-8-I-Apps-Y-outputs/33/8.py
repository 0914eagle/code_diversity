
def solve(sequences):
    # Initialize the result variables
    result_i, result_j = -1, -1
    result_x, result_y = -1, -1
    
    # Iterate over each pair of sequences
    for i in range(len(sequences)):
        for j in range(i+1, len(sequences)):
            # Get the sums of the two sequences
            sum_i = sum(sequences[i])
            sum_j = sum(sequences[j])
            
            # Check if the sums are equal
            if sum_i == sum_j:
                # If they are equal, return the indices of the two sequences
                result_i = i
                result_j = j
                return "YES\n{0} {1}\n{2} {3}".format(result_i+1, result_x+1, result_j+1, result_y+1)
            else:
                # If they are not equal, try removing elements from each sequence until you find a pair that sums up to the other sequence
                for x in range(len(sequences[i])):
                    for y in range(len(sequences[j])):
                        if sum(sequences[i][:x] + sequences[i][x+1:]) == sum(sequences[j][:y] + sequences[j][y+1:]):
                            # If a pair is found, return the indices of the two sequences and the removed elements
                            result_i = i
                            result_j = j
                            result_x = x
                            result_y = y
                            return "YES\n{0} {1}\n{2} {3}".format(result_i+1, result_x+1, result_j+1, result_y+1)
    
    # If no pair is found, return "NO"
    return "NO"

