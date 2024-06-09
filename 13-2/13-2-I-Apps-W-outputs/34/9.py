
import math

def get_army_strength(army):
    # Calculate the greatest common divisor (gcd) of the army strengths
    gcd = math.gcd(army[0], army[1])
    for i in range(2, len(army)):
        gcd = math.gcd(gcd, army[i])
    
    # Calculate the strength of the army by summing the strength of all possible clans
    army_strength = 0
    for i in range(len(army)):
        for j in range(i+1, len(army)):
            if army[i] < army[j] and math.gcd(army[i], army[j]) > 1:
                army_strength += gcd * math.gcd(army[i], army[j])
    
    # Return the modulo of the army strength
    return army_strength % 1000000007

