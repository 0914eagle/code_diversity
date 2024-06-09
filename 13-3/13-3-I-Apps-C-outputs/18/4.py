
def is_possible(W, S, C, K):
    # Initialize the number of each item on the left bank as W, S, and C respectively
    left_bank = [W, S, C]
    
    # Initialize the number of each item in the boat as 0
    boat = [0, 0, 0]
    
    # Loop through each item and check if it can be transferred to the boat
    for i in range(3):
        # If the item is not zero and the boat has space, transfer the item to the boat
        if left_bank[i] > 0 and boat[i] < K:
            boat[i] += left_bank[i]
            left_bank[i] = 0
    
    # Check if all items have been transferred to the boat
    if sum(boat) == W + S + C:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    W, S, C, K = map(int, input().split())
    print(is_possible(W, S, C, K))

