
def get_max_candies(a, b, c):
    # Calculate the maximum number of candies that Alice can have
    max_candies = max(a, b, c)
    
    # If Alice has more candies than Bob, she discards some candies so that the number of candies she has is equal to the number of candies Bob has
    if a > b:
        a = b
    if b > c:
        b = c
    
    # Return the maximum number of candies Alice can have after the division
    return max_candies

