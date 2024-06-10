
def get_match_status(player1, player2, symbol):
    if symbol == ">":
        return 1
    elif symbol == "=":
        return 0
    else:
        return -1

def check_consistency(matches):
    num_players = len(matches)
    player_skills = [0] * num_players
    for match in matches:
        player1, player2, symbol = match
        player1_skill = player_skills[player1]
        player2_skill = player_skills[player2]
        match_status = get_match_status(player1_skill, player2_skill, symbol)
        if match_status == 1:
            player_skills[player1] += 1
            player_skills[player2] -= 1
        elif match_status == 0:
            player_skills[player1] += 0.5
            player_skills[player2] += 0.5
        else:
            return "inconsistent"
    
    for skill in player_skills:
        if skill < 0:
            return "inconsistent"
    
    return "consistent"

def main():
    num_players, num_matches = map(int, input().split())
    matches = []
    for _ in range(num_matches):
        match = input().split()
        matches.append(match)
    
    print(check_consistency(matches))

if __name__ == '__main__':
    main()

