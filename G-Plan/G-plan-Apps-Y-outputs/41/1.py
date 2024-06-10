
def select_runners(n, runners):
    runners.sort(key=lambda x: x[1])  # Sort runners based on their time for the 1st leg
    team = [runners[0]]  # Start with the fastest runner for the 1st leg
    for i in range(1, 4):
        team.append(min(runners, key=lambda x: x[i + 1]))  # Select fastest runner for each subsequent leg
    total_time = sum([runner[i + 1] for i, runner in enumerate(team)])  # Calculate total time
    return total_time, [runner[0] for runner in team]  # Return total time and selected runners


if __name__ == "__main__":
    n = int(input())
    runners = [input().split() for _ in range(n)]
    runners = [(runner[0], float(runner[1]), float(runner[2])) for runner in runners]
    
    total_time, selected_runners = select_runners(n, runners)
    
    print("{:.9f}".format(total_time))
    for runner in selected_runners:
        print(runner)
