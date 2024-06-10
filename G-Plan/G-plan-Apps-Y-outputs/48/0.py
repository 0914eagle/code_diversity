gn_teams(n, skills):
    skills.sort()
    teams = [[] for _ in range(3)]
    total_diversity = 0

    for skill in skills:
        min_diversity = float('inf')
        team_idx = -1

        for i, team in enumerate(teams):
            if len(team) < 3:
                team.append(skill)
                current_diversity = max(team) - min(team)
                if current_diversity < min_diversity:
                    min_diversity = current_diversity
                    team_idx = i
                team.remove(skill)

        teams[team_idx].append(skill)
        total_diversity += min_diversity

    return total_diversity, len(teams), [teams.index(team) + 1 for skill in skills for team in teams if skill in team]


if __name__ == "__main__":
    n = int(input())
    skills = list(map(int, input().split()))

    res, k, team_assignments = assign_teams(n, skills)
    print(res, k)
    print(*team_assignments)
