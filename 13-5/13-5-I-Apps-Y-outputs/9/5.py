
def get_max_problems(difficulties):
    # Sort the difficulties in increasing order
    difficulties.sort()
    # Initialize the maximum number of problems to 1
    max_problems = 1
    # Iterate over the difficulties
    for i in range(len(difficulties)):
        # Check if the difficulty is greater than twice the previous difficulty
        if i > 0 and difficulties[i] > difficulties[i-1]*2:
            # Increment the maximum number of problems
            max_problems += 1
    return max_problems

def main():
    # Read the number of problems and their difficulties from stdin
    num_problems = int(input())
    difficulties = list(map(int, input().split()))
    # Get the maximum number of problems
    max_problems = get_max_problems(difficulties)
    # Print the maximum number of problems
    print(max_problems)

if __name__ == '__main__':
    main()

