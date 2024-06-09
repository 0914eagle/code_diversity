
def get_k_special_table(n, k):
    # Initialize a list to store the table
    table = []
    
    # Initialize a list to store the numbers from 1 to n^2
    numbers = [i for i in range(1, n**2 + 1)]
    
    # Shuffle the list of numbers to randomize the table
    import random
    random.shuffle(numbers)
    
    # Fill the table with the shuffled numbers
    for i in range(n):
        table.append(numbers[i * n : (i + 1) * n])
    
    # Sort the table by row to ensure that the numbers are in increasing order
    table = sorted(table)
    
    # Find the maximum possible sum in the k-th column
    max_sum = sum(table[k - 1])
    
    return max_sum, table

