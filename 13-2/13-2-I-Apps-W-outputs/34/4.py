
import math

def get_strength(army):
    # Sort the army in non-decreasing order
    army.sort()
    # Initialize the strength of the army to 0
    strength = 0
    # Iterate through the army and find the clans
    for i in range(len(army)):
        # Find the gcd of the current soldier and all the previous soldiers
        gcd = math.gcd(army[i], *army[:i])
        # If the gcd is greater than 1, add the strength of the clan to the total strength
        if gcd > 1:
            strength += gcd * (i + 1)
    # Return the modulo of the strength
    return strength % 1000000007

