
def get_minimum_amount(n, debts):
    # Initialize a dictionary to store the debts
    debt_dict = {}
    for i in range(n):
        debt_dict[i+1] = 0
    
    # Iterate through the debts and update the dictionary
    for i in range(n):
        person, amount = debts[i]
        debt_dict[person] += amount
    
    # Find the maximum debt and the person who owes it
    max_debt = max(debt_dict.values())
    person_with_max_debt = [key for key, value in debt_dict.items() if value == max_debt][0]
    
    # Initialize a set to store the people who have paid back their debts
    paid_back_set = set()
    
    # Initialize a variable to store the total amount paid back
    total_amount_paid_back = 0
    
    # Iterate until all debts are paid back
    while len(paid_back_set) < n:
        # Find the person who owes the most money and the amount they owe
        person_with_max_debt = max(debt_dict, key=debt_dict.get)
        amount_owed = debt_dict[person_with_max_debt]
        
        # Pay back as much as possible
        amount_to_pay_back = min(amount_owed, max_debt - total_amount_paid_back)
        total_amount_paid_back += amount_to_pay_back
        
        # Update the dictionary
        debt_dict[person_with_max_debt] -= amount_to_pay_back
        paid_back_set.add(person_with_max_debt)
    
    # Return the total amount paid back
    return total_amount_paid_back

