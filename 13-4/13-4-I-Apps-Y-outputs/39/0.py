
import sys

def solve(problems, drinks):
    # Initialize the time it takes to solve all problems to 0
    total_time = 0

    # Loop through each problem
    for problem in problems:
        # Check if the problem is affected by the drink
        if problem in drinks:
            # If the problem is affected, add the stimulated time to the total time
            total_time += drinks[problem]
        else:
            # If the problem is not affected, add the original time to the total time
            total_time += problem

    # Return the total time it takes to solve all problems
    return total_time

# Read the number of problems and the problems from stdin
num_problems = int(input())
problems = list(map(int, input().split()))

# Read the number of drinks and the drinks from stdin
num_drinks = int(input())
drinks = {}
for i in range(num_drinks):
    problem, stimulated_time = map(int, input().split())
    drinks[problem] = stimulated_time

# Loop through each drink and calculate the total time it takes to solve all problems if Joisino takes that drink
for drink in drinks:
    print(solve(problems, {drink: drinks[drink]}))

