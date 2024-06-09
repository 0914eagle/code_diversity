
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
                # Check if the player has already played the maximum number of matches
                if matches_played[i] == n-1 or matches_played[j] == n-1:
                    return -1
                # Assign the match to the next available day
                for k in range(n):
                    if len(matches_per_day[k]) < n-1:
                        matches_per_day[k].append((i, j))
                        matches_played[i] += 1
                        matches_played[j] += 1
                        break
    
    # Check if all players have played the maximum number of matches
    for i in range(1, n+1):
        if matches_played[i] != n-1:
            return -1
    
    # Return the minimum number of days required
    return len(set(matches_per_day))

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
                # Check if the player has already played the maximum number of matches
                if matches_played[i] == n-1 or matches_played[j] == n-1:
                    return -1
                # Assign the match to the next available day
                for k in range(n):
                    if len(matches_per_day[k]) < n-1:
                        matches_per_day[k].append((i, j))
                        matches_played[i] += 1
                        matches_played[j] += 1
                        break
    
    # Check if all players have played the maximum number of matches
    for i in range(1, n+1):
        if matches_played[i] != n-1:
            return -1
    
    # Return the minimum number of days required
    return len(set(matches_per_day))

if __name__ == '__main__':
    n = int(input())
    matches = []
    for i in range(n):
        matches.append(list(map(int, input().split())))
    print(f1(n, matches))
    print(f2(n, matches))

