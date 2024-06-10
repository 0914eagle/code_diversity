ct_runners(n, runners):
    runners.sort(key=lambda x: x[1])  # Sort runners based on their time for the 1st leg
    team = [runners[0]]  # Start with the fastest runner for the 1st leg
    for i in range(1, 4):
        team.append(min(runners, key=lambda x: x[i + 1]))  # Select the fastest for the next legs
    return team

if __name__ == "__main__":
    n = int(input())
    runners = []
    for _ in range(n):
        name, time1, time2 = input().split()
        runners.append((name, float(time1), float(time2)))
    
    best_team = select_runners(n, runners)
    total_time = sum(runner[1] for runner in best_team)  # Calculate total time
    
    print(round(total_time, 2))
    for runner in best_team:
        print(runner[0])  # Output the names of the selected runners
