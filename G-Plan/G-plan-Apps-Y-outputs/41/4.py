ct_best_team(n, runners):
    runners.sort(key=lambda x: x[1])  # Sort runners based on their time for the 1st leg
    best_team = [runners[0]]  # Start with the fastest runner for the 1st leg

    for i in range(1, 4):
        best_team.append(min((r for r in runners if r not in best_team), key=lambda x: x[i+1]))

    total_time = sum(runner[i+1] for i, runner in enumerate(best_team))
    return total_time, [runner[0] for runner in best_team]


if __name__ == "__main__":
    n = int(input())
    runners = [input().split() for _ in range(n)]
    runners = [(runner[0], float(runner[1]), float(runner[2])) for runner in runners]

    total_time, selected_runners = select_best_team(n, runners)
    print(f"{total_time:.2f}")
    for runner in selected_runners:
        print(runner)
