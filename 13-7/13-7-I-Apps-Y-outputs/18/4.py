
def get_maximum_candies(a, b, c):
    # Calculate the sum of the candies in the three piles
    total_candies = a + b + c
    
    # Alice takes the pile with the most candies
    if a >= b and a >= c:
        alice_candies = a
    elif b >= a and b >= c:
        alice_candies = b
    else:
        alice_candies = c
    
    # Bob takes the pile with the second most candies
    if b >= a and b >= c:
        bob_candies = b
    elif a >= b and a >= c:
        bob_candies = a
    else:
        bob_candies = c
    
    # Calculate the number of candies Alice has to discard to have the same number of candies as Bob
    candies_to_discard = alice_candies - bob_candies
    
    # Calculate the maximum number of candies Alice can have after the division
    maximum_candies = total_candies - candies_to_discard
    
    return maximum_candies

