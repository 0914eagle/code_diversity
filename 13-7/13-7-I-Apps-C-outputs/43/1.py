
def is_winning_strategy(n, k, ancient_numbers):
    # Check if k is one of the ancient numbers
    if k in ancient_numbers:
        return "Yes"
    
    # Check if there is any number in the ancient numbers that is a factor of k
    for num in ancient_numbers:
        if k % num == 0:
            return "Yes"
    
    # Check if there is any number in the ancient numbers that has the same remainder as k when divided by another number in the ancient numbers
    for i in range(len(ancient_numbers)):
        for j in range(i+1, len(ancient_numbers)):
            if ancient_numbers[i] % ancient_numbers[j] == 0:
                return "Yes"
    
    # If none of the above conditions are met, then Arya does not have a winning strategy
    return "No"

