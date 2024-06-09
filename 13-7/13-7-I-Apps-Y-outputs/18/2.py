
def get_maximum_candies(a, b, c):
    # Calculate the sum of the candies in the three piles
    total_candies = a + b + c
    
    # Calculate the maximum number of candies that Alice can have
    # by choosing the pile with the most candies
    max_alice_candies = max(a, b, c)
    
    # Calculate the minimum number of candies that Alice can have
    # by choosing the pile with the least candies and splitting the remaining candies equally between herself and Bob
    min_alice_candies = (total_candies - max_alice_candies) // 2
    
    # Return the maximum number of candies that Alice can have
    return max_alice_candies

