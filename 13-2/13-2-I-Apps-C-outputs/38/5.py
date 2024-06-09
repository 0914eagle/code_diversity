
def get_minimum_transactions(num_people, receipts):
    # Initialize a dictionary to store the amount owed by each person
    amounts_owed = {i: 0 for i in range(num_people)}

    # Iterate over the receipts and update the amounts owed by each person
    for receipt in receipts:
        amounts_owed[receipt[0]] -= receipt[2]
        amounts_owed[receipt[1]] += receipt[2]

    # Initialize a set to store the transactions that need to be made
    transactions = set()

    # Iterate over the amounts owed and create transactions for each negative amount
    for i in range(num_people):
        if amounts_owed[i] < 0:
            transactions.add((i, (i+1)%num_people, -amounts_owed[i]))

    return len(transactions)

def main():
    num_people, num_receipts = map(int, input().split())
    receipts = []
    for _ in range(num_receipts):
        receipts.append(tuple(map(int, input().split())))
    print(get_minimum_transactions(num_people, receipts))

if __name__ == '__main__':
    main()

