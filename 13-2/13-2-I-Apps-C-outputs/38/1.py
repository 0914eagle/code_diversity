
def get_minimum_transactions(receipts):
    # Initialize a dictionary to store the amount owed by each person
    amounts_owed = {}
    for receipt in receipts:
        person1, person2, amount = receipt
        # If the person hasn't been added to the dictionary, add them with the amount they owe
        if person1 not in amounts_owed:
            amounts_owed[person1] = -amount
        # If the person has been added to the dictionary, update their amount owed
        else:
            amounts_owed[person1] -= amount
        # If the person hasn't been added to the dictionary, add them with the amount they owe
        if person2 not in amounts_owed:
            amounts_owed[person2] = amount
        # If the person has been added to the dictionary, update their amount owed
        else:
            amounts_owed[person2] += amount
    
    # Initialize a set to store the transactions
    transactions = set()
    # Loop through the dictionary of amounts owed
    for person, amount in amounts_owed.items():
        # If the amount is non-zero, add a transaction for that person
        if amount != 0:
            transactions.add((person, -amount))
    
    # Return the number of transactions needed
    return len(transactions)

def main():
    # Read the input data
    M, N = map(int, input().split())
    receipts = []
    for _ in range(N):
        receipt = tuple(map(int, input().split()))
        receipts.append(receipt)
    
    # Call the function to get the minimum number of transactions
    minimum_transactions = get_minimum_transactions(receipts)
    
    # Print the output
    print(minimum_transactions)

if __name__ == '__main__':
    main()

