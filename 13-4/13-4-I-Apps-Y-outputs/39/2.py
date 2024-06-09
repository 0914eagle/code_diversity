
def solve(problems, drinks):
    # Initialize a dictionary to store the time it takes to solve each problem
    times = {}

    # Loop through each problem and calculate the time it takes to solve it
    for i, t in enumerate(problems, 1):
        times[i] = t

    # Loop through each drink and calculate the time it takes to solve all problems
    for i, (p, x) in enumerate(drinks, 1):
        # Calculate the time it takes to solve each problem with the given drink
        for j in range(1, len(problems) + 1):
            if j == p:
                times[j] += x

        # Calculate the total time it takes to solve all problems with the given drink
        total_time = sum(times.values())

        # Print the result
        print(f"If Joisino takes drink {i}, it will take her {total_time} seconds to solve all problems.")

# Main function
if __name__ == "__main__":
    # Read the input
    N = int(input())
    problems = list(map(int, input().split()))
    M = int(input())
    drinks = [tuple(map(int, input().split())) for _ in range(M)]

    # Solve the problem
    solve(problems, drinks)

