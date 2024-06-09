
def solve(N, debts):
    # Initialize a dictionary to store the debts
    debt_dict = {}
    for i in range(N):
        debt_dict[i+1] = debts[i]
    
    # Initialize a set to store the people who have paid back their debts
    paid_back = set()
    
    # Initialize a variable to store the total amount of money needed
    total_amount = 0
    
    # Loop until all debts are paid back
    while len(paid_back) < N:
        # Find the person with the highest debt who has not paid back their debt
        highest_debt = -1
        person = -1
        for i in range(1, N+1):
            if i not in paid_back and debt_dict[i] > highest_debt:
                highest_debt = debt_dict[i]
                person = i
        
        # Pay back the debt of the person with the highest debt
        total_amount += highest_debt
        paid_back.add(person)
        
        # Update the debts of the people who owe money to the person who just paid back their debt
        for i in range(1, N+1):
            if i not in paid_back and debt_dict[i] > 0:
                debt_dict[i] -= highest_debt
    
    return total_amount

