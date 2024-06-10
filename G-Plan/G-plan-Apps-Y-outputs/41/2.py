ct_best_team(n, runners):
    runners.sort(key=lambda x: x[1])  # Sort runners based on their time for the 1st leg
    team = [runners[0]]  # Select the fastest runner for the 1st leg
    for i in range(1, 4):
        team.append(min(runners, key=lambda x: x[i+1]))  # Select the fastest runner for the next legs
    total_time = sum([runner[i+1] for i, runner in enumerate(team)])  # Calculate total time
    return total_time, [runner[0] for runner in team]

if __name__ == "__main__":
    n = int(input())
    runners = [input().split() for _ in range(n)]
    runners = [(runner[0], float(runner[1]), float(runner[2])) for runner in runners]
    
    best_time, best_team = select_best_team(n, runners)
    print(best_time)
    for runner in best_team:
        print(runner) 
