
def f1(n, matches):
    # Initialize a dictionary to store the number of matches played by each player
    matches_played = {}
    for i in range(1, n+1):
        matches_played[i] = 0
    
    # Initialize a list to store the matches played by each player on each day
    matches_per_day = []
    for i in range(n):
        matches_per_day.append([])
    
    # Iterate through the matches and assign them to days
    for i in range(n):
        for j in range(i+1, n):
            if matches[i][j] == 1:
                # Check if the player has already played too many matches
                if matches_played[i] >= 1 or matches_played[j] >= 1:
                    return -1
                # Assign the match to a day
                matches_per_day[matches_played[i]].append((i, j))
                matches_played[i] += 1
                matches_played[j] += 1
    
    # Check if all players have played the required number of matches
    for i in range(1, n+1):
        if matches_played[i] != 1:
            return -1
    
    # Calculate the minimum number of days required
    min_days = 0
    for day in matches_per_day:
        if len(day) > 0:
            min_days += 1
    
    return min_days

def f2(n, matches):
    # Initialize a dictionary to store the number of matches played by each player
    matches_played = {}
    for i in range(1, n+1):
        matches_played[i] = 0
    
    # Initialize a list to store the matches played by each player on each day
    matches_per_day = []
    for i in range(n):
        matches_per_day.append([])
    
    # Iterate through the matches and assign them to days
    for i in range(n):
        for j in range(i+1, n):
            if matches[i][j] == 1:
                # Check if the player has already played too many matches
                if matches_played[i] >= 1 or matches_played[j] >= 1:
                    return -1
                # Assign the match to a day
                matches_per_day[matches_played[i]].append((i, j))
                matches_played[i] += 1
                matches_played[j] += 1
    
    # Check if all players have played the required number of matches
    for i in range(1, n+1):
        if matches_played[i] != 1:
            return -1
    
    # Calculate the minimum number of days required
    min_days = 0
    for day in matches_per_day:
        if len(day) > 0:
            min_days += 1
    
    return min_days

if __name__ == '__main__':
    n = int(input())
    matches = []
    for i in range(n):
        matches.append(list(map(int, input().split())))
    print(f1(n, matches))
    print(f2(n, matches))

