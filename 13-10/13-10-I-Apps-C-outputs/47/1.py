
def get_winner(match):
    return match[0]

def get_loser(match):
    return match[1]

def get_matches(matches):
    winner_matches = {}
    loser_matches = {}
    for match in matches:
        winner = get_winner(match)
        loser = get_loser(match)
        if winner not in winner_matches:
            winner_matches[winner] = []
        if loser not in loser_matches:
            loser_matches[loser] = []
        winner_matches[winner].append(match)
        loser_matches[loser].append(match)
    return winner_matches, loser_matches

def is_consistent(matches):
    winner_matches, loser_matches = get_matches(matches)
    for winner, winner_match in winner_matches.items():
        if len(winner_match) > 1:
            return False
    for loser, loser_match in loser_matches.items():
        if len(loser_match) > 1:
            return False
    return True

def main():
    num_players, num_matches = map(int, input().split())
    matches = []
    for _ in range(num_matches):
        match = list(map(int, input().split()))
        matches.append(match)
    if is_consistent(matches):
        print("consistent")
    else:
        print("inconsistent")

if __name__ == '__main__':
    main()

