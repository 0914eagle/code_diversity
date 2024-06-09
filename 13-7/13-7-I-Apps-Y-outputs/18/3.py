
def get_max_candies(a, b, c):
    # Calculate the sum of the three piles
    total = a + b + c
    
    # Find the middle pile with the most candies
    if a >= b and a >= c:
        mid = a
    elif b >= a and b >= c:
        mid = b
    else:
        mid = c
    
    # Calculate the number of candies Alice can have after taking the middle pile
    alice_candies = mid + (total - mid) // 2
    
    # Return the maximum number of candies Alice can have
    return alice_candies

