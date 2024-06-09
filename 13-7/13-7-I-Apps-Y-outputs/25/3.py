
def solve(problems, drinks):
    # Initialize a dictionary to store the time it takes to solve each problem
    problem_time = {}
    for problem in problems:
        problem_time[problem] = problems[problem]

    # Iterate through each drink and calculate the total time to solve all problems
    for drink in drinks:
        total_time = 0
        for problem in problems:
            if problem in drinks[drink]:
                total_time += drinks[drink][problem]
            else:
                total_time += problem_time[problem]
        print(total_time)

def main():
    # Read the input
    num_problems = int(input())
    problems = {}
    for i in range(num_problems):
        problems[i+1] = int(input())

    num_drinks = int(input())
    drinks = {}
    for i in range(num_drinks):
        drinks[i+1] = {}
        num_problems_affected = int(input())
        for j in range(num_problems_affected):
            problem, time = map(int, input().split())
            drinks[i+1][problem] = time

    # Solve the problem
    solve(problems, drinks)

if __name__ == '__main__':
    main()

