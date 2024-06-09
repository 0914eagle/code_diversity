
def is_possible(W, S, C, K):
    # Initialize the number of each item on the bank as W, S, and C
    bank = [W, S, C]
    
    # Initialize the number of items in the boat as 0
    boat = [0, 0, 0]
    
    # Loop until all items are transported
    while sum(bank) > 0:
        # Find the index of the item that is not in the boat and has the most number of items
        index = bank.index(max(bank))
        
        # If the item is a wolf and there are sheep in the boat, move the sheep to the bank
        if index == 0 and boat[1] > 0:
            bank[1] += boat[1]
            boat[1] = 0
        
        # If the item is a sheep and there are cabbages in the boat, move the cabbages to the bank
        elif index == 1 and boat[2] > 0:
            bank[2] += boat[2]
            boat[2] = 0
        
        # If the item is a cabbage and there are wolves in the boat, move the wolves to the bank
        elif index == 2 and boat[0] > 0:
            bank[0] += boat[0]
            boat[0] = 0
        
        # Add the item to the boat if it is not full
        if boat[index] < K:
            boat[index] += 1
            bank[index] -= 1
    
    # If all items are transported and there are no items left on the bank, return YES
    if sum(bank) == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    W, S, C, K = map(int, input().split())
    print(is_possible(W, S, C, K))

