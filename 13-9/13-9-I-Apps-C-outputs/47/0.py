
import math
import itertools

def get_probability_of_g_as_substring(g, k, p):
    
    # Initialize the probability of g being a substring of s as 0
    prob = 0
    
    # Iterate over all possible strings s of length 100
    for s in itertools.product('HT', repeat=100):
        # Check if g is a substring of s
        if g in ''.join(s):
            # Calculate the probability of g being a substring of s
            prob += math.pow(p, len(g)) * math.pow((1-p), (100-len(g)))
    
    return prob

def get_probability_of_g_winning(g, k, p):
    
    # Calculate the probability that g is a substring of the string s
    prob_g_substring = get_probability_of_g_as_substring(g, k, p)
    
    # Calculate the probability that k is a substring of the string s
    prob_k_substring = 1 - prob_g_substring
    
    # Calculate the probability that Gon wins
    prob_g_wins = prob_g_substring / (prob_g_substring + prob_k_substring)
    
    return prob_g_wins

def main():
    g = input("Enter Gon's string: ")
    k = input("Enter Killua's string: ")
    p = float(input("Enter the probability of head: "))
    
    print("Probability that Gon wins:", get_probability_of_g_winning(g, k, p))

if __name__ == '__main__':
    main()

