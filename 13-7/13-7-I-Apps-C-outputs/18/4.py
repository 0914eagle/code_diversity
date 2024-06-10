
def get_max_executives(briefcases):
    # Sort the briefcases in non-decreasing order of banana count
    briefcases.sort()
    # Initialize the number of executives to be rewarded as 0
    num_executives = 0
    # Iterate through the briefcases from least to most evil
    for briefcase in briefcases:
        # If the current briefcase has at least one banana, reward an executive with it
        if briefcase >= 1:
            num_executives += 1
    # Return the maximum number of executives that can be rewarded
    return num_executives

def main():
    # Read the number of briefcases and their banana counts from stdin
    num_briefcases = int(input())
    briefcases = [int(input()) for _ in range(num_briefcases)]
    # Call the get_max_executives function and print the result
    print(get_max_executives(briefcases))

if __name__ == '__main__':
    main()

