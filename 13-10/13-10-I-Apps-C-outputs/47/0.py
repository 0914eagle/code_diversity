
def is_consistent(match_list):
    # Initialize a dictionary to store the skill levels of each player
    skill_levels = {}
    for match in match_list:
        # If the match is a draw, set the skill levels of both players to 0
        if match[1] == '=':
            skill_levels[match[0]] = 0
            skill_levels[match[2]] = 0
        # If the match is a win, set the skill level of the winner to 1 and the skill level of the loser to -1
        else:
            skill_levels[match[0]] = 1
            skill_levels[match[2]] = -1
    
    # Check if the skill levels of all players add up to 0
    total_skill_level = sum(skill_levels.values())
    return total_skill_level == 0

def main():
    # Read the number of players and matches from stdin
    num_players, num_matches = map(int, input().split())
    
    # Read the list of matches from stdin
    match_list = []
    for _ in range(num_matches):
        match = list(map(int, input().split()))
        match_list.append(match)
    
    # Determine if the list of matches is consistent
    if is_consistent(match_list):
        print("consistent")
    else:
        print("inconsistent")

if __name__ == '__main__':
    main()

