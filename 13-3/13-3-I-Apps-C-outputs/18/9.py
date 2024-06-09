
def is_possible(W, S, C, K):
    # Initialize the number of each item on the left bank as W, S, and C respectively
    left_bank = [W, S, C]
    
    # Initialize the number of each item in the boat as 0
    boat = [0, 0, 0]
    
    # Initialize the number of items that can be transferred in total as K
    total_transfer = K
    
    # Loop until all items are transferred
    while sum(left_bank) > 0:
        # Find the index of the item that is not 0 in the left bank
        index = left_bank.index(max(left_bank))
        
        # If the item is a wolf, it can be transferred to the boat
        if index == 0:
            # If the boat is already full, return NO
            if sum(boat) == K:
                return "NO"
            # Add the wolf to the boat
            boat[index] += 1
        
        # If the item is a sheep, it can be transferred to the boat if there is at least one wolf in the boat
        elif index == 1:
            # If there is no wolf in the boat, return NO
            if boat[0] == 0:
                return "NO"
            # Add the sheep to the boat
            boat[index] += 1
        
        # If the item is a cabbage, it can be transferred to the boat if there is at least one sheep in the boat
        elif index == 2:
            # If there is no sheep in the boat, return NO
            if boat[1] == 0:
                return "NO"
            # Add the cabbage to the boat
            boat[index] += 1
        
        # Update the number of items that can be transferred in total
        total_transfer -= 1
        
        # If the boat is full, transfer all items from the boat to the left bank
        if sum(boat) == K:
            left_bank = [sum(left_bank) - sum(boat), 0, 0]
            boat = [0, 0, 0]
    
    # If all items are transferred, return YES
    return "YES"

if __name__ == '__main__':
    W, S, C, K = map(int, input().split())
    print(is_possible(W, S, C, K))

