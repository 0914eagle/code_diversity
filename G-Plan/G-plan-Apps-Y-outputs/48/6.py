gn_teams(n, skills):
    teams = []
    total_diversity = 0
    teams_count = 0
    team_assignments = [0] * n

    sorted_skills = sorted(enumerate(skills), key=lambda x: x[1])

    for i, (index, skill) in enumerate(sorted_skills):
        if i < 3:
            teams.append([skill])
            teams_count += 1
            team_assignments[index] = teams_count
        else:
            min_diversity = float('inf')
            min_index = -1
            for j, team in enumerate(teams):
                diversity = max(team) - min(team)
                if diversity < min_diversity:
                    min_diversity = diversity
                    min_index = j
            teams[min_index].append(skill)
            team_assignments[index] = min_index + 1

        total_diversity += max(teams[team_assignments[index] - 1]) - min(teams[team_assignments[index] - 1])

    return total_diversity, teams_count, team_assignments


if __name__ == "__main__":
    n = int(input())
    skills = list(map(int, input().split()))

    res, k, assignments = assign_teams(n, skills)

    print(res, k)
    print(*assignments)
