ct_best_team(n, runners):
    runners.sort(key=lambda x: x[1])  # Sort runners based on their time for the 1st leg
    team = [runners[0]]  # Start with the fastest runner for the 1st leg
    for i in range(1, 4):
        team.append(min(runners, key=lambda x: x[i+1]))  # Select the fastest runner for each subsequent leg
    total_time = sum(runner[i+1] for i, runner in enumerate(team))  # Calculate total time for the team
    return total_time, [runner[0] for runner in team]  # Return total time and names of selected runners


if __name__ == "__main__":
    n = int(input())
    runners = []
    for _ in range(n):
        name, time_1st_leg, time_other_leg = input().split()
        runners.append((name, float(time_1st_leg), float(time_other_leg)))
    
    total_time, selected_runners = select_best_team(n, runners)
    print(total_time)
    for runner in selected_runners:
        print(runner