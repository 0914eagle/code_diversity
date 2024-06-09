
def k_special_table(n, k):
    # Initialize a list to store the table
    table = []
    
    # Initialize a list to store the numbers from 1 to n^2
    numbers = [i for i in range(1, n**2 + 1)]
    
    # Initialize a list to store the sums of the columns
    column_sums = [0] * n
    
    # Iterate through the rows
    for i in range(n):
        # Initialize a list to store the numbers in the current row
        row = []
        
        # Iterate through the columns
        for j in range(n):
            # Get the next number from the list of numbers
            num = numbers.pop(0)
            
            # Add the number to the current row
            row.append(num)
            
            # Add the number to the sum of the current column
            column_sums[j] += num
        
        # Add the current row to the table
        table.append(row)
    
    # Find the maximum sum of the k-th column
    max_sum = max(column_sums)
    
    # Return the table and the maximum sum
    return table, max_sum

