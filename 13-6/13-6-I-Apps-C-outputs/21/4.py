
def is_winning_strategy(n, k, ancient_numbers):
    # Check if k is one of the ancient numbers
    if k in ancient_numbers:
        return "Yes"
    
    # Check if there is any number that is not in the set of ancient numbers
    # and has the same remainder as k when divided by any of the ancient numbers
    for i in range(1, n+1):
        if i not in ancient_numbers and i % k == 0:
            return "No"
    
    # If we reach this point, then Arya can understand the value of x mod k
    return "Yes"

