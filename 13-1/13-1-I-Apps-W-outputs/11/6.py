
def is_schedulable(matches):
    # Initialize a dictionary to store the number of matches played by each player
    matches_played = {}
    for match in matches:
        for player in match:
            if player not in matches_played:
                matches_played[player] = 1
            else:
                matches_played[player] += 1

    # Check if all players have played the maximum number of matches
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

    # Sort the matches by the number of matches played by the first player
    sorted_matches = sorted(matches, key=lambda x: matches_played[x[0]])

    # Schedule the matches
    schedule = []
    for match in sorted_matches:
        schedule.append(match)
        matches_played[match[0]] += 1
        matches_played[match[1]] += 1

    return schedule

def main():
    num_players = int(input())
    matches = []
    for _ in range(num_players):
        match = list(map(int, input().split()))
        matches.append(match)

    if is_schedulable(matches):
        schedule = schedule_matches(matches)
        print(len(schedule))
    else:
        print(-1)

if __name__ == '__main__':
    main()

