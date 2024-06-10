
def select_runners(n, runners):
    runners.sort(key=lambda x: x[1])  # Sort based on time for the 1st leg
    team = [runners[0]]  # Start with the fastest for the 1st leg
    for i in range(1, 4):
        team.append(min(runners, key=lambda x: x[i+1]))  # Select fastest for each leg
    total_time = sum(runner[i+1] for i, runner in enumerate(team))
    return total_time, [runner[0] for runner in team]

if __name__ == "__main__":
    n = int(input())
    runners = [input().split() for _ in range(n)]
    runners = [(runner[0], float(runner[1]), float(runner[2])) for runner in runners]
    time, selected_runners = select_runners(n, runners)
    print("{:.9f}".format(time))
    for runner in selected_runners:
        print(runner)
