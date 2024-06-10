
def consistent_report(matches):
    # Initialize a dictionary to store the results of each match
    results = {}
    
    # Iterate over the matches and store the results in the dictionary
    for match in matches:
        k, symbol, l = match
        if symbol == "=":
            results[k] = results.get(k, 0) + 1
            results[l] = results.get(l, 0) + 1
        else:
            results[k] = results.get(k, 0) + 2
            results[l] = results.get(l, 0) + 2
    
    # Check if any player has a negative result, which means they have lost more games than they have won
    for player, result in results.items():
        if result < 0:
            return "inconsistent"
    
    # If no player has a negative result, the list of matches is consistent
    return "consistent"

def main():
    # Read the number of players and matches from stdin
    n, m = map(int, input().split())
    
    # Read the matches from stdin
    matches = []
    for _ in range(m):
        k, symbol, l = map(int, input().split())
        matches.append((k, symbol, l))
    
    # Call the consistent_report function and print the result
    print(consistent_report(matches))

if __name__ == '__main__':
    main()

