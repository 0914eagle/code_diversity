
def is_schedulable(matches):
    # Initialize a dictionary to store the number of matches played by each player
    matches_played = {}
    for match in matches:
        for player in match:
            if player not in matches_played:
                matches_played[player] = 1
            else:
                matches_played[player] += 1

    # Check if all players have played the required number of matches
    for player, num_matches in matches_played.items():
        if num_matches != len(matches):
            return False

    # Check if all matches are unique
    for i in range(len(matches)):
        for j in range(i+1, len(matches)):
            if matches[i] == matches[j]:
                return False

    return True

def schedule_matches(matches):
    # Initialize a dictionary to store the number of matches played by each player
    matches_played = {}
    for match in matches:
        for player in match:
            if player not in matches_played:
                matches_played[player] = 1
            else:
                matches_played[player] += 1

    # Initialize a list to store the scheduled matches
    scheduled_matches = []

    # Schedule the matches for each player
    for player, num_matches in matches_played.items():
        for i in range(num_matches):
            scheduled_matches.append([player, matches[player-1][i]])

    return scheduled_matches

def main():
    num_players = int(input())
    matches = []
    for i in range(num_players):
        matches.append(list(map(int, input().split())))

    if is_schedulable(matches):
        scheduled_matches = schedule_matches(matches)
        print(len(scheduled_matches))
        for match in scheduled_matches:
            print(match[0], match[1])
    else:
        print(-1)

if __name__ == '__main__':
    main()

