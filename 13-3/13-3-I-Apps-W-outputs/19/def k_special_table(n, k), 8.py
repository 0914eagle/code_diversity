
def k_special_table(n, k):
    # Initialize a list to store the table
    table = []
    
    # Initialize a list to store the numbers from 1 to n^2
    numbers = [i for i in range(1, n**2 + 1)]
    
    # Initialize a list to store the columns of the table
    columns = [[] for _ in range(n)]
    
    # Iterate through the numbers and add them to the table
    for i in range(n):
        # Get the next number from the list of numbers
        number = numbers.pop(0)
        
        # Add the number to the current column
        columns[i].append(number)
        
        # If the current column is the k-th column, add the number to the sum
        if i == k - 1:
            sum += number
    
    # Iterate through the columns and add them to the table
    for column in columns:
        table.append(column)
    
    # Return the table and the sum of the numbers in the k-th column
    return table, sum

