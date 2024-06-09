
def black_vienna(investigations):
    num_investigations = len(investigations)
    num_suspects = 26
    num_solutions = 0
    
    for i in range(num_investigations):
        suspects = investigations[i][:2]
        player = investigations[i][2]
        reply = investigations[i][3]
        
        # Initialize a dictionary to store the number of each suspect in each player's hand
        suspect_counts = {suspect: 0 for suspect in range(1, num_suspects + 1)}
        for suspect in suspects:
            suspect_counts[suspect] += 1
        
        # Update the dictionary with the reply from the current investigation
        suspect_counts[player] -= reply
        
        # Check if the reply is consistent with the number of suspects in each player's hand
        if suspect_counts[player] < 0:
            return 0
        
        # Count the number of admissible solutions
        num_solutions += count_solutions(suspect_counts)
    
    return num_solutions

def count_solutions(suspect_counts):
    num_solutions = 0
    for suspect in range(1, 27):
        if suspect_counts[suspect] == 0:
            continue
        num_solutions += choose(suspect_counts[suspect], 3)
    return num_solutions

def choose(n, k):
    if k < 0 or n < k:
        return 0
    if k == 0 or n == k:
        return 1
    return choose(n - 1, k - 1) + choose(n - 1, k)

