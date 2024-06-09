
def get_min_transactions(num_people, receipts):
    # Initialize a dictionary to store the amount each person owes
    amounts_owed = {i: 0 for i in range(num_people)}

    # Iterate over the receipts and update the amounts owed
    for receipt in receipts:
        amounts_owed[receipt[0]] -= receipt[2]
        amounts_owed[receipt[1]] += receipt[2]

    # Initialize a set to store the transactions
    transactions = set()

    # Iterate over the amounts owed and create transactions
    for i in range(num_people):
        for j in range(i+1, num_people):
            if amounts_owed[i] != 0 and amounts_owed[j] != 0:
                transactions.add((i, j, min(amounts_owed[i], amounts_owed[j])))
                amounts_owed[i] -= min(amounts_owed[i], amounts_owed[j])
                amounts_owed[j] -= min(amounts_owed[i], amounts_owed[j])

    return len(transactions)

def main():
    num_people, num_receipts = map(int, input().split())
    receipts = []
    for _ in range(num_receipts):
        receipts.append(list(map(int, input().split())))
    print(get_min_transactions(num_people, receipts))

if __name__ == '__main__':
    main()

