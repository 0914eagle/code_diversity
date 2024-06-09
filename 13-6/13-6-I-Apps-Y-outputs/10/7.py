
def get_largest_sum(A, K):
    # Sort the array in descending order
    A.sort(reverse=True)
    
    # Initialize the sum and the number of negative numbers
    sum = 0
    num_negative = 0
    
    # Iterate through the array and calculate the sum
    for i in range(len(A)):
        if A[i] < 0:
            num_negative += 1
        sum += A[i]
    
    # If K is odd, we can choose one negative number to make it positive
    if K % 2 == 1 and num_negative > 0:
        sum += A[0]
        K -= 1
    
    # Return the sum
    return sum

def get_largest_sum_after_k_negatives(A, K):
    # Initialize the largest sum
    largest_sum = 0
    
    # Iterate through the array and calculate the sum
    for i in range(len(A)):
        # If the current sum is greater than the largest sum, update the largest sum
        if get_largest_sum(A, K) > largest_sum:
            largest_sum = get_largest_sum(A, K)
    
    # Return the largest sum
    return largest_sum

if __name__ == '__main__':
    A = [4, 2, 3]
    K = 1
    print(get_largest_sum_after_k_negatives(A, K))

    A = [3, -1, 0, 2]
    K = 3
    print(get_largest_sum_after_k_negatives(A, K))

    A = [2, -3, -1, 5, -4]
    K = 2
    print(get_largest_sum_after_k_negatives(A, K))

