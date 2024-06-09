
def get_max_problems(difficulties):
    # Sort the difficulties in increasing order
    difficulties.sort()
    # Initialize the maximum number of problems to 1
    max_problems = 1
    # Iterate over the difficulties
    for i in range(1, len(difficulties)):
        # Check if the difficulty of the current problem is greater than twice the difficulty of the previous problem
        if difficulties[i] > 2 * difficulties[i - 1]:
            # If it is, increment the maximum number of problems
            max_problems += 1
    return max_problems

def main():
    # Read the number of problems and their difficulties from stdin
    num_problems = int(input())
    difficulties = list(map(int, input().split()))
    # Call the get_max_problems function and print the result
    print(get_max_problems(difficulties))

if __name__ == '__main__':
    main()

