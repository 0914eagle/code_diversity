
def solve(N, A, B):
    # Initialize a dictionary to store the debts
    debts = {}

    # Iterate over the input and add the debts to the dictionary
    for i in range(N):
        debts[i + 1] = -B[i]

    # Initialize a set to store the visited nodes
    visited = set()

    # Initialize a variable to store the total amount of money to be given
    total_amount = 0

    # Iterate until all debts are paid
    while debts:
        # Find the person with the maximum debt
        max_debt = max(debts.items(), key=lambda x: x[1])

        # If the person has a negative debt, they have enough money to pay back
        if max_debt[1] < 0:
            # Add the amount they have to the total amount
            total_amount += -max_debt[1]

            # Remove the person from the dictionary
            del debts[max_debt[0]]

            # Add the person to the visited set
            visited.add(max_debt[0])

            # Iterate over the dictionary and update the debts
            for person, debt in debts.items():
                if person not in visited:
                    debts[person] += debt
        else:
            # If the person does not have enough money to pay back, break the loop
            break

    return total_amount

