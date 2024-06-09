
def solve(n, s):
    # Initialize the number of sets to 0
    sets = 0
    # Loop through each possible value of x from 1 to n
    for x in range(1, n+1):
        # If x is 1, then the first set is finished
        if x == 1:
            sets += 1
        # Loop through each round
        for i in range(n):
            # If the current round is won by the other player, break the loop
            if s[i] == "1" and x == 1:
                break
            # If the current round is won by the current player, and the next x rounds are won by the other player, break the loop
            if s[i] == "0" and s[i+1:i+x].count("1") == x:
                break
        # If the loop finished, then the set is finished
        else:
            sets += 1
    # Return the number of sets
    return sets

