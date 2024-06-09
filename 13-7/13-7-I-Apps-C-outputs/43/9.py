
def is_winning_strategy(n, k, ancient_numbers):
    # Check if k is one of the ancient numbers
    if k in ancient_numbers:
        return "Yes"
    
    # Check if any two ancient numbers have a common remainder
    for i in range(n):
        for j in range(i+1, n):
            if ancient_numbers[i] % k == ancient_numbers[j] % k:
                return "Yes"
    
    return "No"

