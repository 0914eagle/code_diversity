
def get_final_ratings(n, ratings):
    # Sort the ratings in descending order
    ratings = sorted(ratings, reverse=True)
    
    # Calculate the difference between the highest and lowest ratings
    diff = ratings[0] - ratings[-1]
    
    # Calculate the number of matches needed to make all ratings equal
    matches = diff // 2
    
    # Create a list to store the matches
    matches_list = []
    
    # Iterate over the ratings and create a list of teams with equal ratings
    for i in range(matches):
        team = []
        for j in range(n):
            team.append(ratings[j] - i)
        matches_list.append(team)
    
    # Return the final ratings and the number of matches
    return ratings, matches_list

def get_match_teams(n, ratings, matches_list):
    # Create a list to store the teams for each match
    teams_list = []
    
    # Iterate over the matches and create a list of teams for each match
    for i in range(len(matches_list)):
        team = []
        for j in range(n):
            if ratings[j] - i >= 0:
                team.append(j)
        teams_list.append(team)
    
    # Return the list of teams for each match
    return teams_list

def get_match_teams_str(n, teams_list):
    # Create a list to store the string representation of the teams for each match
    teams_str_list = []
    
    # Iterate over the teams for each match and create a string representation of the teams
    for team in teams_list:
        teams_str = ''
        for i in team:
            teams_str += str(i)
        teams_str_list.append(teams_str)
    
    # Return the list of string representations of the teams for each match
    return teams_str_list

def main():
    n = int(input())
    ratings = list(map(int, input().split()))
    final_ratings, matches_list = get_final_ratings(n, ratings)
    teams_list = get_match_teams(n, ratings, matches_list)
    teams_str_list = get_match_teams_str(n, teams_list)
    print(final_ratings)
    print(len(matches_list))
    for team in teams_str_list:
        print(team)

if __name__ == '__main__':
    main()

