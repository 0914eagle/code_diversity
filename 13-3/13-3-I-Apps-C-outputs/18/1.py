
def is_possible(W, S, C, K):
    # Initialize the number of each item on the bank as W, S, and C
    bank = [W, S, C]
    
    # Initialize the number of each item in the boat as 0
    boat = [0, 0, 0]
    
    # Loop until all items are transported
    while sum(bank) > 0:
        # Find the index of the item that is not 0 in the bank
        index = bank.index(max(bank))
        
        # If the item is a wolf, it can be transported without any restrictions
        if index == 0:
            boat[index] += 1
            bank[index] -= 1
        
        # If the item is a sheep, it can be transported if there are no wolves in the boat
        elif index == 1 and boat[0] == 0:
            boat[index] += 1
            bank[index] -= 1
        
        # If the item is a cabbage, it can be transported if there are no wolves or sheep in the boat
        elif index == 2 and boat[0] == 0 and boat[1] == 0:
            boat[index] += 1
            bank[index] -= 1
        
        # If the boat is full, transfer all items to the other bank
        if sum(boat) == K:
            bank[0] += boat[0]
            bank[1] += boat[1]
            bank[2] += boat[2]
            boat = [0, 0, 0]
    
    # If all items are transported and no items are left on the bank, return YES
    if sum(bank) == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    W, S, C, K = map(int, input().split())
    print(is_possible(W, S, C, K))

