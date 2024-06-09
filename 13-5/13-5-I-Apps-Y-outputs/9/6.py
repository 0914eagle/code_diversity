
def get_max_problems(difficulties):
    # Sort the difficulties in increasing order
    difficulties.sort()
    # Initialize the maximum number of problems to 1
    max_problems = 1
    # Initialize the current number of problems to 1
    current_problems = 1
    # Iterate over the difficulties
    for i in range(1, len(difficulties)):
        # If the current difficulty is less than or equal to twice the previous difficulty, increase the current number of problems
        if difficulties[i] <= difficulties[i-1]*2:
            current_problems += 1
        # Otherwise, reset the current number of problems to 1
        else:
            current_problems = 1
        # Update the maximum number of problems if necessary
        max_problems = max(max_problems, current_problems)
    return max_problems

def main():
    n = int(input())
    difficulties = list(map(int, input().split()))
    print(get_max_problems(difficulties))

if __name__ == '__main__':
    main()

