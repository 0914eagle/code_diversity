
def get_minimum_transactions(receipts):
    # Initialize a dictionary to store the net balance of each person
    net_balance = {}
    for person in range(len(receipts)):
        net_balance[person] = 0
    
    # Iterate through the receipts and update the net balance of each person
    for receipt in receipts:
        person1, person2, amount = receipt
        net_balance[person1] -= amount
        net_balance[person2] += amount
    
    # Find the person with the highest net balance and the person with the lowest net balance
    highest_balance = max(net_balance.values())
    lowest_balance = min(net_balance.values())
    
    # Return the difference between the highest and lowest net balance
    return highest_balance - lowest_balance

def main():
    receipts = []
    for _ in range(int(input())):
        receipts.append(list(map(int, input().split())))
    print(get_minimum_transactions(receipts))

if __name__ == '__main__':
    main()

