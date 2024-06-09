
def get_largest_sum(A, K):
    # Sort the array in descending order
    A.sort(reverse=True)
    
    # Initialize the sum and the number of negative numbers
    sum = 0
    num_neg = 0
    
    # Iterate through the array and update the sum and the number of negative numbers
    for i in range(len(A)):
        if A[i] < 0:
            num_neg += 1
        sum += A[i]
    
    # Return the sum if K is 0 or the number of negative numbers is 0
    if K == 0 or num_neg == 0:
        return sum
    
    # Initialize the maximum sum
    max_sum = 0
    
    # Iterate through the array and try all possible combinations of negative numbers
    for i in range(num_neg + 1):
        # Get the sum of the positive numbers
        pos_sum = sum - i * A[0]
        
        # Get the sum of the negative numbers
        neg_sum = i * A[0]
        
        # Update the maximum sum
        max_sum = max(max_sum, pos_sum + neg_sum)
    
    # Return the maximum sum
    return max_sum

