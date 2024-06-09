
def get_min_transactions(receipts):
    # Initialize a dictionary to store the net balance of each person
    net_balance = {i: 0 for i in range(len(receipts))}
    
    # Iterate over the receipts and update the net balance of each person
    for receipt in receipts:
        net_balance[receipt[0]] -= receipt[2]
        net_balance[receipt[1]] += receipt[2]
    
    # Initialize a set to store the transactions
    transactions = set()
    
    # Iterate over the net balance of each person and add the transactions to the set
    for i in range(len(net_balance)):
        for j in range(i+1, len(net_balance)):
            if net_balance[i] != 0 and net_balance[j] != 0 and net_balance[i] != net_balance[j]:
                transactions.add((i, j))
    
    # Return the number of transactions needed to settle the score
    return len(transactions)

