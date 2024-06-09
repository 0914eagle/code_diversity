
def find_max_sum(a, b, k):
    # Sort the arrays a and b in descending order
    a.sort(reverse=True)
    b.sort(reverse=True)
    
    # Initialize the maximum sum and the number of moves made so far
    max_sum = 0
    moves_made = 0
    
    # Loop through the arrays a and b and find the maximum sum
    for i in range(len(a)):
        for j in range(len(b)):
            # Check if the number of moves made is less than or equal to k
            if moves_made <= k:
                # Add the product of the two numbers to the maximum sum
                max_sum += a[i] * b[j]
                # Increment the number of moves made
                moves_made += 1
            else:
                # If the number of moves made is greater than k, break the loop
                break
    
    # Return the maximum sum
    return max_sum

