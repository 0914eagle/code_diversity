
def check_consistency(matches):
    # Initialize a dictionary to store the skill levels of each player
    skills = {}
    for match in matches:
        # If the symbol is '=', set the skill level of both players to 0
        if match[1] == '=':
            skills[match[0]] = 0
            skills[match[2]] = 0
        # If the symbol is '>', set the skill level of the winner to 1 and the skill level of the loser to -1
        elif match[1] == '>':
            skills[match[0]] = 1
            skills[match[2]] = -1
    
    # Check if the sum of the skill levels of all players is 0
    if sum(skills.values()) != 0:
        return "inconsistent"
    else:
        return "consistent"

def main():
    # Read the number of players and matches from stdin
    num_players, num_matches = map(int, input().split())
    
    # Read the matches from stdin
    matches = []
    for _ in range(num_matches):
        match = list(map(int, input().split()))
        matches.append(match)
    
    # Call the check_consistency function and print the result
    result = check_consistency(matches)
    print(result)

if __name__ == '__main__':
    main()

