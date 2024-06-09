
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
    
    # Initialize a variable to store the total amount of money given to the town
    total_amount = 0
    
    # Loop through the dictionary and calculate the minimum amount of money needed to pay back all debts
    while len(paid_back) < N:
        for person, debt in debt_dict.items():
            if debt == 0 and person not in paid_back:
                paid_back.add(person)
                total_amount += debt_dict[person]
    
    return total_amount

