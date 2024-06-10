
import math

def game(g, k, p):
    # Initialize variables
    g_idx = 0
    k_idx = 0
    s = ""
    turns = 0
    gon_wins = 0
    killua_wins = 0
    draws = 0

    # Loop until the game ends or the maximum number of turns is reached
    while g_idx < len(g) and k_idx < len(k) and turns < 10**100:
        # Flip a coin
        if math.random() < p:
            s += "H"
        else:
            s += "T"

        # Update the indices of g and k in s
        g_idx = s.find(g, g_idx)
        k_idx = s.find(k, k_idx)

        # Check if Gon or Killua has won
        if g_idx < len(g) and k_idx < len(k):
            # Both strings are substrings of s, draw
            draws += 1
        elif g_idx < len(g):
            # Gon has won
            gon_wins += 1
        elif k_idx < len(k):
            # Killua has won
            killua_wins += 1

        # Increment turns
        turns += 1

    # Return the probability of Gon winning
    return gon_wins / turns

def main():
    # Read input from stdin
    g = input()
    k = input()
    p = float(input())

    # Call the game function and print the result
    print(game(g, k, p))

if __name__ == '__main__':
    main()

