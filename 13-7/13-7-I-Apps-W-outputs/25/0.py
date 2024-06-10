
def get_team_count(seating_plan):
    team_count = {}
    for seat in seating_plan:
        if seat not in team_count:
            team_count[seat] = 1
        else:
            team_count[seat] += 1
    return team_count

def get_min_switches(seating_plan):
    team_count = get_team_count(seating_plan)
    min_switches = 0
    for team in team_count:
        if team_count[team] > 1:
            min_switches += team_count[team] - 1
    return min_switches

def main():
    n = int(input())
    seating_plan = input()
    print(get_min_switches(seating_plan))

if __name__ == '__main__':
    main()

