
def get_prettiness(problems):
    # Sort the problems in descending order
    problems.sort(reverse=True)
    # Initialize the maximum prettiness as 0
    max_prettiness = 0
    # Loop through the problems
    for i in range(len(problems)):
        # Get the current problem's prettiness
        curr_prettiness = problems[i]
        # Check if the current problem's prettiness is divisible by any of the previous problems
        for j in range(i):
            if curr_prettiness % problems[j] == 0:
                break
        else:
            # If the current problem's prettiness is not divisible by any of the previous problems, add it to the maximum prettiness
            max_prettiness += curr_prettiness
    return max_prettiness

def main():
    # Read the number of queries
    q = int(input())
    # Loop through the queries
    for _ in range(q):
        # Read the number of problems
        n = int(input())
        # Read the prettinesses of the problems
        problems = list(map(int, input().split()))
        # Get the maximum prettiness of the contest composed of at most three problems
        max_prettiness = get_prettiness(problems[:3])
        # Print the maximum prettiness
        print(max_prettiness)

if __name__ == '__main__':
    main()

