
def k_special_table(n, k):
    # Initialize a list to store the table
    table = []
    
    # Initialize a list to store the numbers from 1 to n^2
    numbers = [i for i in range(1, n**2 + 1)]
    
    # Initialize a list to store the columns of the table
    columns = [[] for _ in range(n)]
    
    # Iterate through the numbers and add them to the table
    for i in range(n):
        # Find the maximum number in the current column
        max_num = max(numbers)
        
        # Add the maximum number to the current column
        columns[i].append(max_num)
        
        # Remove the maximum number from the list of numbers
        numbers.remove(max_num)
    
    # Sort the numbers in increasing order
    numbers.sort()
    
    # Add the numbers to the table in the order they appear in the list
    for i in range(n):
        table.append(numbers[i])
    
    # Return the sum of the numbers in the k-th column
    return sum(table[k-1])

