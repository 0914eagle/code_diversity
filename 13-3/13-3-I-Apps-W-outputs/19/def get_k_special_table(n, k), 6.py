
def get_k_special_table(n, k):
    # Initialize a list to store the table
    table = []
    
    # Initialize a list to store the numbers from 1 to n^2
    numbers = [i for i in range(1, n**2 + 1)]
    
    # Initialize a list to store the sums of the columns
    column_sums = [0] * n
    
    # Loop through the numbers and add them to the table
    for i in range(n):
        # Get the next number from the list of numbers
        number = numbers.pop(0)
        
        # Add the number to the table
        table.append(number)
        
        # Update the sum of the column
        column_sums[i % n] += number
    
    # Find the maximum sum of the column
    max_column_sum = max(column_sums)
    
    # Return the table and the maximum sum of the column
    return table, max_column_sum

