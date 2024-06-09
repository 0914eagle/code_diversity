
def solve(problems, drinks):
    # Initialize a dictionary to store the time it takes to solve each problem
    times = {}

    # Loop through each problem and calculate the time it takes to solve it
    for i, t in enumerate(problems, start=1):
        times[i] = t

    # Loop through each drink and calculate the time it takes to solve all problems if we take that drink
    for i, (p, x) in enumerate(drinks, start=1):
        # Initialize a variable to store the total time it takes to solve all problems
        total_time = 0

        # Loop through each problem and calculate the time it takes to solve it if we take the drink
        for j in range(1, len(problems) + 1):
            if j == p:
                total_time += x
            else:
                total_time += times[j]

        # Print the total time it takes to solve all problems if we take the drink
        print(total_time)

# Main function
if __name__ == "__main__":
    # Read the number of problems and the time it takes to solve each problem from stdin
    num_problems = int(input())
    problems = list(map(int, input().split()))

    # Read the number of drinks and the problem and time it takes to solve each problem if we take that drink from stdin
    num_drinks = int(input())
    drinks = [list(map(int, input().split())) for _ in range(num_drinks)]

    # Solve the problem
    solve(problems, drinks)

