
def game_of_coins(g, k, p):
    # Initialize the probability of Gon winning as 0
    probability_gwon = 0
    
    # Loop through each possible substring of length 1 to 20 of the coin flip string
    for i in range(1, 21):
        # Get the probability of Gon winning for the current substring length
        probability_gwon += probability_gwon_substring(g, k, i, p)
    
    # Return the probability of Gon winning
    return probability_gwon

def probability_gwon_substring(g, k, i, p):
    # Initialize the probability of Gon winning as 0
    probability_gwon = 0
    
    # Loop through each possible substring of length i of the coin flip string
    for j in range(len(g) - i + 1):
        # Get the probability of Gon winning for the current substring
        probability_gwon += probability_gwon_substring_helper(g, k, j, i, p)
    
    # Return the probability of Gon winning for the current substring length
    return probability_gwon

def probability_gwon_substring_helper(g, k, j, i, p):
    # Initialize the probability of Gon winning as 0
    probability_gwon = 0
    
    # Loop through each possible coin flip result for the current substring
    for l in range(i):
        # Get the probability of Gon winning for the current substring and coin flip result
        probability_gwon += probability_gwon_substring_helper_helper(g, k, j, i, l, p)
    
    # Return the probability of Gon winning for the current substring and coin flip result
    return probability_gwon

def probability_gwon_substring_helper_helper(g, k, j, i, l, p):
    # Initialize the probability of Gon winning as 0
    probability_gwon = 0
    
    # If the current substring and coin flip result match Gon's string
    if g[j:j+i] == g:
        # Return the probability of Gon winning
        return p**l * (1-p)**(i-l)
    
    # If the current substring and coin flip result match Killua's string
    elif k[j:j+i] == k:
        # Return the probability of Killua winning
        return (1-p)**l * p**(i-l)
    
    # Otherwise, return 0
    else:
        return 0

if __name__ == '__main__':
    g = input()
    k = input()
    p = float(input())
    print(game_of_coins(g, k, p))

