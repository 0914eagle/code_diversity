
def solve(N, debts):
    # Initialize a dictionary to store the debts
    debt_dict = {}
    for i in range(N):
        debt_dict[i+1] = 0
    
    # Add the debts to the dictionary
    for debt in debts:
        debt_dict[debt[0]] += debt[1]
        debt_dict[debt[1]] -= debt[1]
    
    # Initialize a set to store the people who have paid back their debts
    paid_back = set()
    
    # Initialize a variable to store the total amount of money needed
    total_amount = 0
    
    # Loop through the dictionary and calculate the total amount of money needed
    for person, amount in debt_dict.items():
        if amount > 0:
            total_amount += amount
    
    return total_amount

