
def solve(n, arr):
    # Calculate the sum of the array
    sum = 0
    for i in range(n):
        sum += arr[i]
    
    # If the sum is odd, it is not possible to break the chocolate into pieces with exactly one nut
    if sum % 2 == 1:
        return 0
    
    # Initialize the number of ways to break the chocolate
    ways = 0
    
    # Iterate through all possible combinations of pieces with and without nuts
    for i in range(1 << n):
        # Initialize the number of nuts in the current combination
        num_nuts = 0
        
        # Iterate through the pieces in the current combination
        for j in range(n):
            # If the current piece has a nut, add it to the number of nuts
            if i & (1 << j):
                num_nuts += 1
        
        # If the number of nuts is equal to the sum of the array, add the current combination to the number of ways
        if num_nuts == sum // 2:
            ways += 1
    
    return ways

