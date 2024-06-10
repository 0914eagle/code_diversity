ct_runners(n, runners):
    runners.sort(key=lambda x: x[1])  # Sort runners based on their time for the 1st leg
    team = [runners[0]]  # Start with the fastest runner for the 1st leg
    for i in range(1, 4):
        team.append(min(runners, key=lambda x: x[i+1]))  # Select the fastest runner for each subsequent leg
    total_time = sum([runner[i+1] for i, runner in enumerate(team)])  # Calculate total time for the team
    return total_time, [runner[0] for runner in team]

if __name__ == "__main__":
    n = int(input())
    runners = []
    for _ in range(n):
        name, time_1st, time_other = input().split()
        runners.append((name, float(time_1st), float(time_other)))
    
    best_time, best_team = select_runners(n, runners)
    print(best_time)
    for runner in best_team:
        print(runner