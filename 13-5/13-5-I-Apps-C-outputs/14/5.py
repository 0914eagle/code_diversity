
def get_minimum_amount(n, debts):
    # Initialize a dictionary to store the debts
    debt_dict = {}
    for i in range(n):
        debt_dict[i+1] = debts[i]
    
    # Initialize a set to store the visited individuals
    visited = set()
    
    # Initialize a variable to store the minimum amount
    min_amount = 0
    
    # Loop through the dictionary until all debts are paid
    while len(debt_dict) > 0:
        # Find the individual with the minimum debt
        min_debt = float('inf')
        min_debt_individual = 0
        for individual, debt in debt_dict.items():
            if debt < min_debt and individual not in visited:
                min_debt = debt
                min_debt_individual = individual
        
        # Add the minimum debt to the minimum amount
        min_amount += min_debt
        
        # Remove the individual with the minimum debt from the dictionary
        del debt_dict[min_debt_individual]
        
        # Add the individual to the visited set
        visited.add(min_debt_individual)
    
    # Return the minimum amount
    return min_amount

