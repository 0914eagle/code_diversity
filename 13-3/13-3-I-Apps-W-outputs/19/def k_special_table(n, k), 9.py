
def k_special_table(n, k):
    # Initialize a list to store the table
    table = []
    
    # Initialize a set to store the numbers that have been used
    used_numbers = set()
    
    # Loop through each row of the table
    for i in range(n):
        # Initialize a list to store the numbers in the current row
        row = []
        
        # Loop through each column of the current row
        for j in range(n):
            # Calculate the number for the current cell
            number = (i * n) + j + 1
            
            # If the number has not been used, add it to the row and mark it as used
            if number not in used_numbers:
                row.append(number)
                used_numbers.add(number)
            # If the number has been used, find the next available number and add it to the row
            else:
                for num in range(number + 1, n * n + 1):
                    if num not in used_numbers:
                        row.append(num)
                        used_numbers.add(num)
                        break
        
        # Add the current row to the table
        table.append(row)
    
    # Calculate the sum of the numbers in the k-th column
    sum_k = sum(table[k - 1])
    
    # Return the table and the sum of the numbers in the k-th column
    return table, sum_k

