
def solve(N, A, B):
    # Initialize a dictionary to store the debts
    debts = {}

    # Iterate over the input and populate the dictionary
    for i in range(N):
        debts[i+1] = -B[i]

    # Initialize a set to store the people who have paid back their debts
    paid_back = set()

    # Initialize a variable to store the total amount of money given by the town
    total_amount = 0

    # Iterate until all debts are paid back
    while len(paid_back) < N:
        # Find the person who owes the most money
        max_debt = max(debts.values())

        # Find the person who owes the most money and has not paid back their debt yet
        for person in debts:
            if debts[person] == max_debt and person not in paid_back:
                break

        # Pay back the debt of the person who owes the most money
        debts[person] = 0
        paid_back.add(person)

        # Check if the person who paid back their debt has enough money to pay back the debts of others
        if person in debts and debts[person] < 0:
            # Give the person enough money to pay back their debts
            total_amount += -debts[person]
            debts[person] = 0

    return total_amount

