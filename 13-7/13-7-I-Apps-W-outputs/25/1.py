
def get_team_count(team_string):
    team_count = {}
    for team in team_string:
        if team not in team_count:
            team_count[team] = 1
        else:
            team_count[team] += 1
    return team_count

def get_min_switches(team_string):
    team_count = get_team_count(team_string)
    min_switches = 0
    for team in team_count:
        if team_count[team] > 1:
            min_switches += team_count[team] - 1
    return min_switches

def main():
    team_string = input()
    print(get_min_switches(team_string))

if __name__ == '__main__':
    main()

